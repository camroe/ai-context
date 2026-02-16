---
applyTo: '**'
---

# Next.js Best Practices for LLMs (2026)

_Last updated: February 2026 - Next.js 16+_

This document summarizes the latest, authoritative best practices for building, structuring, and maintaining Next.js 16+ applications. It is intended for use by LLMs and developers to ensure code quality, maintainability, and scalability.

## Version Requirements
- **Next.js:** 16.0+ (Current: 16.1.6)
- **Node.js:** 20.9+ (LTS)
- **TypeScript:** 5.1+
- **React:** 19.2+ (included with Next.js 16)
- **Browsers:** Chrome 111+, Edge 111+, Firefox 111+, Safari 16.4+

---

## 1. Project Structure & Organization

- **Use the `app/` directory** (App Router) for all new projects. Prefer it over the legacy `pages/` directory.
- **Top-level folders:**
  - `app/` — Routing, layouts, pages, and route handlers
  - `public/` — Static assets (images, fonts, etc.)
  - `lib/` — Shared utilities, API clients, and logic
  - `components/` — Reusable UI components
  - `contexts/` — React context providers
  - `styles/` — Global and modular stylesheets
  - `hooks/` — Custom React hooks
  - `types/` — TypeScript type definitions
- **Colocation:** Place files (components, styles, tests) near where they are used, but avoid deeply nested structures.
- **Route Groups:** Use parentheses (e.g., `(admin)`) to group routes without affecting the URL path.
- **Private Folders:** Prefix with `_` (e.g., `_internal`) to opt out of routing and signal implementation details.

- **Feature Folders:** For large apps, group by feature (e.g., `app/dashboard/`, `app/auth/`).
- **Use `src/`** (optional): Place all source code in `src/` to separate from config files.

## 2.1. Server and Client Component Integration (App Router)

**Cache Components and Dynamic Rendering:**
- **Default behavior in Next.js 16:** All dynamic code executes at request time by default (no implicit caching)
- **Opt-in caching:** Use `"use cache"` directive for explicit caching
- **Never use `next/dynamic` with `{ ssr: false }` inside a Server Component** - Not supported

**Correct Approach:**
- Move client-only logic into dedicated Client Components (with `'use client'`)
- Import Client Components directly in Server Components
- Use Cache Components for performance-critical sections

**Cache Components Example:**
```tsx
"use cache"
export async function ExpensiveServerComponent() {
  const data = await fetch('/api/data')
  return <div>{data}</div>
}
```

**Example:**

```tsx
// Server Component
import DashboardNavbar from '@/components/DashboardNavbar';

export default async function DashboardPage() {
  // ...server logic...
  return (
    <>
      <DashboardNavbar /> {/* This is a Client Component */}
      {/* ...rest of server-rendered page... */}
    </>
  );
}
```

**Why:**
- Server Components cannot use client-only features or dynamic imports with SSR disabled.
- Client Components can be rendered inside Server Components, but not the other way around.

**Summary:**
Always move client-only UI into a Client Component and import it directly in your Server Component. Never use `next/dynamic` with `{ ssr: false }` in a Server Component.

---

## 2. Component Best Practices

- **Component Types:**
  - **Server Components** (default): For data fetching, heavy logic, and non-interactive UI.
  - **Client Components:** Add `'use client'` at the top. Use for interactivity, state, or browser APIs.
- **When to Create a Component:**
  - If a UI pattern is reused more than once.
  - If a section of a page is complex or self-contained.
  - If it improves readability or testability.
- **Naming Conventions:**
  - Use `PascalCase` for component files and exports (e.g., `UserCard.tsx`).
  - Use `camelCase` for hooks (e.g., `useUser.ts`).
  - Use `snake_case` or `kebab-case` for static assets (e.g., `logo_dark.svg`).
  - Name context providers as `XyzProvider` (e.g., `ThemeProvider`).
- **File Naming:**
  - Match the component name to the file name.
  - For single-export files, default export the component.
  - For multiple related components, use an `index.ts` barrel file.
- **Component Location:**
  - Place shared components in `components/`.
  - Place route-specific components inside the relevant route folder.
- **Props:**
  - Use TypeScript interfaces for props.
  - Prefer explicit prop types and default values.
- **Testing:**
  - Co-locate tests with components (e.g., `UserCard.test.tsx`).

## 3. Naming Conventions (General)

- **Folders:** `kebab-case` (e.g., `user-profile/`)
- **Files:** `PascalCase` for components, `camelCase` for utilities/hooks, `kebab-case` for static assets
- **Variables/Functions:** `camelCase`
- **Types/Interfaces:** `PascalCase`
- **Constants:** `UPPER_SNAKE_CASE`

## 4. API Routes (Route Handlers) & Proxy Configuration

### Route Handlers
- **Location:** Place API routes in `app/api/` (e.g., `app/api/users/route.ts`)
- **HTTP Methods:** Export async functions named after HTTP verbs (`GET`, `POST`, etc.)
- **Parameters:** Use `await params` and `await searchParams` (breaking change in v16)
- **Server Functions:** Use `await cookies()`, `await headers()`, `await draftMode()`
- **Validation:** Always validate with `zod` or similar libraries

**Example with async parameters:**
```tsx
export async function GET(request: Request, { params }: { params: Promise<{ id: string }> }) {
  const { id } = await params // Must await in Next.js 16+
  const searchParams = await request.searchParams // If needed
  return Response.json({ id })
}
```

### Proxy Configuration (formerly Middleware)
- **Breaking Change:** `middleware.ts` → `proxy.ts`
- **Runtime:** Node.js runtime (not Edge)
- **Export:** Rename exported function to `proxy`

**Migration:**
```tsx
// proxy.ts (NEW)
export default function proxy(request: NextRequest) {
  return NextResponse.redirect(new URL('/home', request.url))
}

// middleware.ts is deprecated (will be removed)
```

## 5. Cache Components & Modern Caching (Next.js 16)

### Cache Components
- **Enable in config:**
```ts
// next.config.ts
const nextConfig = {
  cacheComponents: true,
}
```

- **Use `"use cache"` directive for explicit caching:**
```tsx
"use cache"
export async function CachedComponent() {
  const data = await expensiveOperation()
  return <div>{data}</div>
}
```

### New Caching APIs
- **`updateTag(tag)`** - Server Actions only, immediate cache refresh with read-your-writes
- **`refresh()`** - Server Actions only, refresh uncached data
- **`revalidateTag(tag, profile)`** - Now requires cacheLife profile for SWR behavior

```tsx
'use server'
import { updateTag, refresh, revalidateTag } from 'next/cache'

// Immediate update (users see changes right away)
export async function updateUserProfile(userId: string, profile: Profile) {
  await db.users.update(userId, profile)
  updateTag(`user-${userId}`)
}

// Background revalidation with SWR
export async function refreshContent() {
  revalidateTag('blog-posts', 'max') // Built-in cacheLife profile
}

// Refresh uncached dynamic data
export async function markNotificationRead(id: string) {
  await db.notifications.markAsRead(id)
  refresh() // Refreshes uncached notification counts etc.
}
```

## 6. Development & Build Experience

### Turbopack (Default in v16)
- **Default bundler** for all new projects (2-5× faster builds, up to 10× faster Fast Refresh)
- **Opt out:** `next dev --webpack` or `next build --webpack`
- **File system caching:** Enable with `experimental.turbopackFileSystemCacheForDev: true`

### React Compiler (Stable)
- **Automatic memoization** with zero manual changes
- **Enable:**
```ts
// next.config.ts
const nextConfig = {
  reactCompiler: true, // Moved from experimental
}
```

## 7. General Best Practices

- **TypeScript:** Strict mode, TypeScript 5.1+ required
- **Build Tools:** Turbopack default, React Compiler for optimization
- **Caching:** Explicit with Cache Components and new APIs
- **Environment:** Node.js 20.9+, modern browsers only
- **Testing:** Playwright, Jest, React Testing Library
- **Performance:**
  - Use Cache Components for expensive operations
  - Leverage enhanced routing with layout deduplication
  - Utilize Turbopack's faster builds and HMR
- **Security:**
  - Use `proxy.ts` for request interception
  - Validate all inputs with proper type checking
  - Utilize new browser security features

# Avoid Unnecessary Example Files

Do not create example/demo files (like ModalExample.tsx) in the main codebase unless the user specifically requests a live example, Storybook story, or explicit documentation component. Keep the repository clean and production-focused by default.

# Always use the latest documentation and guides
- For every nextjs related request, begin by searching for the most current nextjs documentation, guides, and examples.
- Use the following tools to fetch and search documentation if they are available:
  - `resolve_library_id` to resolve the package/library name in the docs.
  - `get_library_docs` for up to date documentation.


