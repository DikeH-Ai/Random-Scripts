#include <cs50.h>
#include <stdio.h>

int get_cents(void);
int calculate_quarters(int cents);
int calculate_dimes(int cents);
int calculate_nickels(int cents);
int calculate_pennies(int cents);

int main(void)
{
    // Ask how many cents the customer is owed
    int cents = get_cents();

    // Calculate the number of quarters to give the customer
    int quarters = calculate_quarters(cents);
    cents = cents - quarters * 25;

    // Calculate the number of dimes to give the customer
    int dimes = calculate_dimes(cents);
    cents = cents - dimes * 10;

    // Calculate the number of nickels to give the customer
    int nickels = calculate_nickels(cents);
    cents = cents - nickels * 5;

    // Calculate the number of pennies to give the customer
    int pennies = calculate_pennies(cents);
    cents = cents - pennies * 1;

    // Sum coins
    int coins = quarters + dimes + nickels + pennies;

    // Print total number of coins to give the customer
    printf("%i\n", coins);
}

int get_cents(void)
{
    // TODO
    int x;
    do
    {
        x = get_int("Change: ");
    }
    while (x <= -1);
    return x;
}

int calculate_quarters(int cents)
{
    // TODO
    int quarters = 25;
    return cents / quarters;
}

int calculate_dimes(int cents)
{
    // TODO
    int dimes = 10;
    return cents / dimes;
}

int calculate_nickels(int cents)
{
    // TODO
    int nickels = 5;
    return cents / nickels;
}

int calculate_pennies(int cents)
{
    // TODO
    int pennies = 1;
    return cents / pennies;
}
