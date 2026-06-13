from ui.calculator_ui import CalculatorUI
from logic.calculator_logic import CalculatorLogic
from database.db import Database

if __name__ == "__main__":
    db = Database()
    logic = CalculatorLogic(db)
    app = CalculatorUI(logic)
    app.run()