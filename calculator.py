#!/usr/bin/env python3
"""
Professional Calculator Implementation
Author: [Your Name]
Date: June 28, 2025
Description: A comprehensive calculator with error handling and professional code standards
"""

import math
import sys
from typing import Union, List, Dict

class Calculator:
    """
    A professional calculator class with comprehensive functionality
    and robust error handling.
    """
    
    def __init__(self):
        """Initialize calculator with operation history and supported operations."""
        self.history: List[str] = []
        self.supported_operations = {
            '+': self.add,
            '-': self.subtract,
            '*': self.multiply,
            '/': self.divide,
            '**': self.power,
            '^': self.power,
            'sqrt': self.square_root,
            'log': self.logarithm,
            'sin': self.sine,
            'cos': self.cosine,
            'tan': self.tangent
        }
    
    def add(self, first_number: float, second_number: float) -> float:
        """
        Perform addition operation.
        
        Args:
            first_number (float): First operand
            second_number (float): Second operand
            
        Returns:
            float: Sum of the two numbers
        """
        return first_number + second_number
    
    def subtract(self, first_number: float, second_number: float) -> float:
        """
        Perform subtraction operation.
        
        Args:
            first_number (float): Minuend
            second_number (float): Subtrahend
            
        Returns:
            float: Difference of the two numbers
        """
        return first_number - second_number
    
    def multiply(self, first_number: float, second_number: float) -> float:
        """
        Perform multiplication operation.
        
        Args:
            first_number (float): First factor
            second_number (float): Second factor
            
        Returns:
            float: Product of the two numbers
        """
        return first_number * second_number
    
    def divide(self, dividend: float, divisor: float) -> Union[float, str]:
        """
        Perform division operation with zero-division error handling.
        
        Args:
            dividend (float): Number to be divided
            divisor (float): Number to divide by
            
        Returns:
            Union[float, str]: Quotient or error message
            
        Raises:
            ZeroDivisionError: When divisor is zero
        """
        try:
            if divisor == 0:
                raise ZeroDivisionError("Cannot divide by zero")
            return dividend / divisor
        except ZeroDivisionError as error:
            return f"Error: {str(error)}"
    
    def power(self, base: float, exponent: float) -> Union[float, str]:
        """
        Calculate base raised to the power of exponent.
        
        Args:
            base (float): Base number
            exponent (float): Exponent
            
        Returns:
            Union[float, str]: Result or error message
        """
        try:
            if base == 0 and exponent < 0:
                raise ValueError("Cannot raise 0 to a negative power")
            result = base ** exponent
            if math.isinf(result):
                return "Error: Result too large (infinity)"
            return result
        except (ValueError, OverflowError) as error:
            return f"Error: {str(error)}"
    
    def square_root(self, number: float) -> Union[float, str]:
        """
        Calculate square root of a number.
        
        Args:
            number (float): Number to find square root of
            
        Returns:
            Union[float, str]: Square root or error message
        """
        try:
            if number < 0:
                raise ValueError("Cannot calculate square root of negative number")
            return math.sqrt(number)
        except ValueError as error:
            return f"Error: {str(error)}"
    
    def logarithm(self, number: float, base: float = math.e) -> Union[float, str]:
        """
        Calculate logarithm of a number.
        
        Args:
            number (float): Number to find logarithm of
            base (float): Base of logarithm (default: natural log)
            
        Returns:
            Union[float, str]: Logarithm or error message
        """
        try:
            if number <= 0:
                raise ValueError("Logarithm undefined for non-positive numbers")
            if base <= 0 or base == 1:
                raise ValueError("Invalid logarithm base")
            return math.log(number, base)
        except ValueError as error:
            return f"Error: {str(error)}"
    
    def sine(self, angle: float, use_degrees: bool = False) -> float:
        """
        Calculate sine of an angle.
        
        Args:
            angle (float): Angle in radians (or degrees if use_degrees=True)
            use_degrees (bool): Whether angle is in degrees
            
        Returns:
            float: Sine of the angle
        """
        if use_degrees:
            angle = math.radians(angle)
        return math.sin(angle)
    
    def cosine(self, angle: float, use_degrees: bool = False) -> float:
        """
        Calculate cosine of an angle.
        
        Args:
            angle (float): Angle in radians (or degrees if use_degrees=True)
            use_degrees (bool): Whether angle is in degrees
            
        Returns:
            float: Cosine of the angle
        """
        if use_degrees:
            angle = math.radians(angle)
        return math.cos(angle)
    
    def tangent(self, angle: float, use_degrees: bool = False) -> Union[float, str]:
        """
        Calculate tangent of an angle.
        
        Args:
            angle (float): Angle in radians (or degrees if use_degrees=True)
            use_degrees (bool): Whether angle is in degrees
            
        Returns:
            Union[float, str]: Tangent of the angle or error message
        """
        if use_degrees:
            angle = math.radians(angle)
        
        # Check for angles where tangent is undefined (odd multiples of π/2)
        normalized_angle = angle % (2 * math.pi)
        if abs(normalized_angle - math.pi/2) < 1e-10 or abs(normalized_angle - 3*math.pi/2) < 1e-10:
            return "Error: Tangent undefined at this angle"
        
        return math.tan(angle)
    
    def validate_input(self, user_input: str) -> Union[float, str]:
        """
        Validate and convert user input to float.
        
        Args:
            user_input (str): User input string
            
        Returns:
            Union[float, str]: Converted number or error message
        """
        try:
            # Remove whitespace and validate
            cleaned_input = user_input.strip()
            if not cleaned_input:
                raise ValueError("Empty input provided")
            
            # Convert to float
            number = float(cleaned_input)
            
            # Check for infinity and NaN
            if math.isinf(number):
                raise ValueError("Number too large")
            if math.isnan(number):
                raise ValueError("Invalid number format")
            
            return number
        except ValueError as error:
            return f"Input Error: {str(error)}"
    
    def format_result(self, result: Union[float, str]) -> str:
        """
        Format calculation result for display.
        
        Args:
            result (Union[float, str]): Calculation result
            
        Returns:
            str: Formatted result string
        """
        if isinstance(result, str):
            return result  # Error message, return as-is
        
        # Handle integer results
        if isinstance(result, float) and result.is_integer():
            return str(int(result))
        
        # Round to reasonable precision and remove trailing zeros
        formatted = f"{result:.10g}"
        return formatted
    
    def add_to_history(self, operation: str, result: str) -> None:
        """
        Add operation to calculation history.
        
        Args:
            operation (str): The operation performed
            result (str): The result of the operation
        """
        history_entry = f"{operation} = {result}"
        self.history.append(history_entry)
        
        # Keep only last 10 operations
        if len(self.history) > 10:
            self.history.pop(0)
    
    def show_history(self) -> None:
        """Display calculation history."""
        if not self.history:
            print("No calculation history available.")
            return
        
        print("\n--- Calculation History ---")
        for i, entry in enumerate(self.history, 1):
            print(f"{i:2d}. {entry}")
        print("-" * 25)
    
    def clear_history(self) -> None:
        """Clear calculation history."""
        self.history.clear()
        print("Calculation history cleared.")
    
    def perform_basic_operation(self) -> None:
        """Handle basic two-operand operations."""
        print("\nAvailable operations: +, -, *, /, ** (or ^)")
        
        # Get first number
        first_input = input("Enter first number: ")
        first_number = self.validate_input(first_input)
        if isinstance(first_number, str):
            print(first_number)
            return
        
        # Get operation
        operation = input("Enter operation (+, -, *, /, **, ^): ").strip()
        if operation not in ['+', '-', '*', '/', '**', '^']:
            print("Error: Invalid operation")
            return
        
        # Get second number
        second_input = input("Enter second number: ")
        second_number = self.validate_input(second_input)
        if isinstance(second_number, str):
            print(second_number)
            return
        
        # Perform calculation
        if operation in self.supported_operations:
            result = self.supported_operations[operation](first_number, second_number)
            formatted_result = self.format_result(result)
            
            # Display and store result
            operation_string = f"{first_number} {operation} {second_number}"
            print(f"Result: {formatted_result}")
            self.add_to_history(operation_string, formatted_result)
    
    def perform_single_operand_operation(self) -> None:
        """Handle single-operand operations (sqrt, log, trig functions)."""
        print("\nAvailable functions: sqrt, log, sin, cos, tan")
        
        function = input("Enter function: ").strip().lower()
        if function not in ['sqrt', 'log', 'sin', 'cos', 'tan']:
            print("Error: Invalid function")
            return
        
        # Get number
        number_input = input("Enter number: ")
        number = self.validate_input(number_input)
        if isinstance(number, str):
            print(number)
            return
        
        # Handle specific function requirements
        if function == 'log':
            base_input = input("Enter base (press Enter for natural log): ").strip()
            if base_input:
                base = self.validate_input(base_input)
                if isinstance(base, str):
                    print(base)
                    return
                result = self.logarithm(number, base)
                operation_string = f"log_{base}({number})"
            else:
                result = self.logarithm(number)
                operation_string = f"ln({number})"
        elif function in ['sin', 'cos', 'tan']:
            degree_input = input("Use degrees? (y/n, default: radians): ").strip().lower()
            use_degrees = degree_input == 'y'
            result = self.supported_operations[function](number, use_degrees)
            unit = "°" if use_degrees else " rad"
            operation_string = f"{function}({number}{unit})"
        else:
            result = self.supported_operations[function](number)
            operation_string = f"{function}({number})"
        
        # Display and store result
        formatted_result = self.format_result(result)
        print(f"Result: {formatted_result}")
        self.add_to_history(operation_string, formatted_result)
    
    def display_menu(self) -> None:
        """Display main calculator menu."""
        print("\n" + "="*50)
        print("           PROFESSIONAL CALCULATOR")
        print("="*50)
        print("1. Basic Operations (+, -, *, /, **)")
        print("2. Advanced Functions (sqrt, log, trig)")
        print("3. Show History")
        print("4. Clear History")
        print("5. Help")
        print("6. Exit")
        print("-"*50)
    
    def show_help(self) -> None:
        """Display help information."""
        help_text = """
CALCULATOR HELP GUIDE
====================

BASIC OPERATIONS:
  Addition (+):         5 + 3 = 8
  Subtraction (-):      10 - 4 = 6
  Multiplication (*):   6 * 7 = 42
  Division (/):         15 / 3 = 5
  Power (** or ^):      2 ** 3 = 8

ADVANCED FUNCTIONS:
  Square Root:          sqrt(16) = 4
  Logarithm:           log(100, 10) = 2
  Natural Log:         ln(e) = 1
  Trigonometric:       sin(90°) = 1

ERROR HANDLING:
  • Division by zero is prevented
  • Invalid inputs are caught and reported
  • Mathematical errors are handled gracefully

FEATURES:
  • Calculation history (last 10 operations)
  • High precision arithmetic
  • Both degree and radian modes for trig functions
  • Input validation and error recovery
        """
        print(help_text)
    
    def run(self) -> None:
        """Main calculator loop."""
        print("Welcome to the Professional Calculator!")
        print("Type numbers carefully and follow the prompts.")
        
        while True:
            try:
                self.display_menu()
                choice = input("Select option (1-6): ").strip()
                
                if choice == '1':
                    self.perform_basic_operation()
                elif choice == '2':
                    self.perform_single_operand_operation()
                elif choice == '3':
                    self.show_history()
                elif choice == '4':
                    self.clear_history()
                elif choice == '5':
                    self.show_help()
                elif choice == '6':
                    print("\nThank you for using Professional Calculator!")
                    print("Goodbye!")
                    break
                else:
                    print("Error: Please select a valid option (1-6)")
                
                # Pause before showing menu again
                if choice != '6':
                    input("\nPress Enter to continue...")
                    
            except KeyboardInterrupt:
                print("\n\nCalculator interrupted by user.")
                print("Goodbye!")
                break
            except Exception as unexpected_error:
                print(f"Unexpected error occurred: {str(unexpected_error)}")
                print("Please try again or restart the calculator.")


def main():
    """
    Main function to run the calculator application.
    Handles command line arguments and initializes the calculator.
    """
    try:
        # Create and run calculator instance
        calculator = Calculator()
        calculator.run()
    except Exception as error:
        print(f"Fatal error: {str(error)}")
        print("Calculator could not start. Please check your Python installation.")
        sys.exit(1)


if __name__ == "__main__":
    main()