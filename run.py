from web_app import create_app
import os
from dotenv import load_dotenv

load_dotenv()
app = create_app()

DEBUG_ENV_VAR = os.getenv("FLASK_DEBUG")
print(f"Debug Config: {DEBUG_ENV_VAR}")
if DEBUG_ENV_VAR and DEBUG_ENV_VAR.lower() in ("true", "1", "t", "y", "yes"):
    app.config["DEBUG"] = True
    print("Flask DEBUG is ON.")
else:
    app.config["DEBUG"] = False
    print("Flask DEBUG is OFF.")

if __name__ == "__main__":
    app.run(debug=app.config["DEBUG"])