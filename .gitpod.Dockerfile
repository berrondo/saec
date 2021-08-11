FROM gitpod/workspace-postgres

ENV DEBUG=0
ENV SECRET_KEY=SomERandonKey02301084mfa
ENV ALLOWED_HOSTS=".gitpod.io, 127.0.0.1, .localhost"
ENV DJANGO_DB_HOST=localhost
ENV POSTGRES_DB=postgres
ENV POSTGRES_USER=gitpod
ENV POSTGRES_PASSWORD=pg

