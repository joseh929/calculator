#include <stdio.h>
#include<stdlib.h>
#include<math.h>
#define MAX_HISTORY 100
#define MAX_LINE 100
int main(){
    double num1,num2;  // Variables to store user input numbers
    int oper;   // Variable to store user's choice of operation
    char again,ask_again;  // Variable to ask user if they want to perform another calculation
    char history[MAX_HISTORY][MAX_LINE];
int historyCount = 0;
    do{
            // Display menu option
        printf("MENU\n");
    printf("1. Addition (+)\n"
            "2. Subtraction (-)\n"
            "3. Multiplication (*)\n"
            "4. Division (/)\n"
            "5. power (x^y)\n"
            "6. Square Root\n"
            "7. Percentage \n"
            "8. view calculation history\n"
            "9. Exit\n"
            );
    //ask user to select an operation in the above menu
    printf("choose operation(1-9)\n");
    scanf("%d",&oper);
    //exit operation
    if(oper==9){
        printf("exiting calculator.\n");
        break;
    }
    if(oper==6){
            //Square root operation only requires one number
        printf("enter a number:\n");
        scanf("%lf",&num1);
        if(num1<0){
                // cannot take sqrt of negative numbers
            printf("ERROR!.Cannot take square root of a negative number.\n");
        }
        else{
            printf("result=%.2lf\n",sqrt(num1));
            snprintf(history[historyCount++], MAX_LINE, "√%.2lf = %.2lf", num1, sqrt(num1));
        }
         // Ask user if they want to do another operation
            printf("Continue to another operation? (y/n): \n");
            scanf(" %c", &again);
            continue;  // Go back to top of the loop
    }
    // Handle operations that require special input or conditions
        //Also it ask for the two numbers to be operated on from user
         if (oper >= 1 && oper <= 5 || oper == 7) {
    printf("enter first number: \n");
    scanf("%lf",&num1);
    printf("enter second number: \n");
    scanf("%lf",&num2);
         }
    switch(oper){
    case 1:
        printf("result=%.2lf\n",num1+num2);
         snprintf(history[historyCount++], MAX_LINE, "%.2lf + %.2lf = %.2lf", num1, num2, num1 + num2);
        break;
    case 2:
        printf("result=%.2lf\n",num1-num2);
        snprintf(history[historyCount++], MAX_LINE, "%.2lf - %.2lf = %.2lf", num1, num2, num1 - num2);
        break;
    case 3:
        printf("result=%.2lf\n",num1*num2);
        snprintf(history[historyCount++], MAX_LINE, "%.2lf * %.2lf = %.2lf", num1, num2, num1 * num2);
        break;
    case 4:
        if(num2==0){
                //Division by zero is an infinity number hence a math error
            printf("error!!! division by zero.\n");
              }else{
        printf("result=%.2lf\n",num1/num2);
          snprintf(history[historyCount++], MAX_LINE, "%.2lf / %.2lf = %.2lf", num1, num2, num1 / num2);
              }
        break;
    case 5:
        printf("result=%.2lf\n",(pow(num1,num2)));
        snprintf(history[historyCount++], MAX_LINE, "%.2lf ^ %.2lf = %.2lf", num1, num2, pow(num1, num2));
        break;
        break;
          case 7:
                printf("%.2lf is %.2lf%% of %.2lf\n", num1, (num1 / num2) * 100, num2);  // Percentage calculation
                   snprintf(history[historyCount++], MAX_LINE, "%.2lf is %.2lf%% of %.2lf", num1, (num1 / num2) * 100, num2);
                break;
        case 8:
        if (historyCount == 0) {
            printf("No calculations yet.\n");
        } else {
            printf("-- Calculation History --\n");
            for (int i = 0; i < historyCount; i++) {
                printf("%d. %s\n", i + 1, history[i]);
            }
            // Ask user if they want to do another operation
            printf("Continue to another operation? (y/n): \n");
            scanf(" %c", &again);
            continue;  // Go back to top of the loop
        }
    default:
        //this handles invalid menu choice
        printf("invalid choice.\n");
    }
    //Ask user if they want to perform another operation
    ask_again;
    printf("continue to another operation?(y/n)\n");
    scanf(" %c",&again);
}while(again == 'y'); //loop continues if user enters'y'which signifies yes and exit the program if'n' is entered which means NO
//end message
printf("Thank you for using the calculator!\n");
return 0; //Exit program
}