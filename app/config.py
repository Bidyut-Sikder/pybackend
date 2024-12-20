from pydantic_settings import BaseSettings
# BaseSettings allows values to be overridden by environment variables.

class Settings(BaseSettings):
    # Use the appropriate data from the .env file
    database_username :str
    database_password :str
    database_host :str  # Use the appropriate host
    database_port :str    # Default PostgreSQL port
    database_name :str
    

    class Config:
        env_file = ".env"  # Optional: Load variables from a .env file

# Initialize settings
settings = Settings()

print(settings)


 
 




