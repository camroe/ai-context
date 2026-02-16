---
description: 'Next.js 16+ + Tailwind development standards and instructions'
applyTo: '**/*.tsx, **/*.ts, **/*.jsx, **/*.js, **/*.css'
---

# Next.js 16+ + Tailwind Development Instructions

Instructions for high-quality Next.js 16+ applications with Tailwind CSS styling and TypeScript.

## Project Context

- **Next.js 16+** with App Router and Turbopack
- **TypeScript 5.1+** for type safety
- **Tailwind CSS** for styling
- **React 19.2+** with latest features
- **Node.js 20.9+** runtime

## Development Standards

### Architecture
- App Router with server and client components
- **Cache Components** for performance (`"use cache"` directive)
- **Proxy.ts** for request interception (not middleware.ts)
- Group routes by feature/domain
- Implement proper error boundaries
- Use React Server Components by default
- Leverage static optimization with explicit caching

### TypeScript
- Strict mode enabled
- Clear type definitions
- Proper error handling with type guards
- Zod for runtime type validation

### Styling
- Tailwind CSS with consistent color palette
- Responsive design patterns
- Dark mode support
- Follow container queries best practices
- Maintain semantic HTML structure

### State Management
- React Server Components for server state
- React hooks for client state
- Proper loading and error states
- Optimistic updates where appropriate

### Data Fetching & Caching
- Server Components for direct database queries
- **Cache Components** with `"use cache"` for expensive operations
- **New caching APIs**: `updateTag()`, `refresh()`, `revalidateTag(tag, profile)`
- React Suspense for loading states
- Proper error handling and retry logic
- **Async parameters**: `await params`, `await searchParams`
- **Async server functions**: `await cookies()`, `await headers()`

### Security
- **Input validation** with Zod schemas and sanitization
- **Proxy.ts** for request interception (replaces middleware.ts)
- **Authentication checks** with proper session handling
- **CSRF protection** for forms and API routes
- **Rate limiting** implementation
- **Secure API route handling** with type validation
- **Environment variables** in .env.local only
- **Content Security Policy** headers

### Performance & Development Experience
- **Turbopack** default bundler (2-5× faster builds, 10× faster HMR)
- **React Compiler** for automatic memoization
- **File system caching** for faster dev startup
- **Enhanced routing** with layout deduplication
- **Image optimization** with next/image
- **Font optimization** with next/font
- **Route prefetching** with improved cache behavior
- **Bundle size optimization** with code splitting

### Next.js 16 Breaking Changes Compliance
- ✅ Use `proxy.ts` instead of deprecated `middleware.ts`
- ✅ Always `await` params, searchParams in route handlers
- ✅ Always `await` cookies(), headers(), draftMode() calls
- ✅ Use `revalidateTag(tag, profile)` with cacheLife profiles
- ✅ Enable `cacheComponents: true` for Cache Components
- ✅ Ensure Node.js 20.9+ and TypeScript 5.1+ compatibility
- ✅ Use modern browser features (Chrome 111+, Safari 16.4+)

## Implementation Process
1. Plan component hierarchy
2. Define types and interfaces
3. Implement server-side logic
4. Build client components
5. Add proper error handling
6. Implement responsive styling
7. Add loading states
8. Write tests
