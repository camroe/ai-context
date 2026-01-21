# PostgreSQL Best Practices for FAA Repair Station Tracking

- Use UUIDs for primary keys to ensure uniqueness across distributed systems.
- Normalize tables to reduce redundancy, but use JSONB columns for flexible, state-specific or audit data.
- Always define foreign key constraints for referential integrity.
- Use GIN indexes on JSONB columns for efficient querying.
- Leverage PostgreSQL roles and permissions for data security and compliance.
- Use timestamp with time zone (timestamptz) for all audit and state change records.
- Regularly back up the database and test restores.
- Use connection pooling for application performance.
- Document schema changes and use migration tools (e.g., Flyway, Liquibase).
- Monitor query performance and tune indexes as needed.
