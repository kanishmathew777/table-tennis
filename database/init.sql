CREATE USER ttadmin WITH ENCRYPTED PASSWORD 'superuser' SUPERUSER CREATEDB CREATEROLE;
CREATE DATABASE ttbackend WITH ENCODING 'UTF8' OWNER ttadmin;
GRANT ALL PRIVILEGES ON DATABASE ttbackend TO ttadmin;
