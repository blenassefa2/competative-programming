#include<iostream>
#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<stack>

using namespace std;

class Game
{
    int move_counter;
    int disc_no;
    bool game_over;
    stack<int> stack1;
    stack<int> stack2;
    stack<int> stack3;

public:
    // Create game and display instructions
    Game()
    {
        this->move_counter = 0;
        this->game_over = false;
        this->instructions();
        
    }
    // Print instructions
    void instructions()
    {
        system("cls");
        
        cout<< "         \t            Welcome to tower of hanoi" \
        "\n         |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||\
        \n         ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||\
        \n         ||||||||||||||||   |||||||||||||   |||||||||||||   |||||||||||||\
        \n         ||||||||||||||||   |||||||||||||   |||||||||||||   |||||||||||||\
        \n         ||||||||||||||||   |||||||||||||   |||||||||||||   |||||||||||||\
        \n         ||||||||||||||   1   |||||||||||   |||||||||||||   |||||||||||||\
        \n         |||||||||||||    2    ||||||||||   |||||||||||||   |||||||||||||\
        \n         ||||||||||||     3     |||||||||   |||||||||||||   |||||||||||||\
        \n         ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||\
        \n         |||||||||||||  stack 1 ||||||  stack 2 ||||||  stack 3 |||||||||\
        \n         ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||\
        \nInstructions:- the point of the game is to finish transfering all stacks from first poll to another\
                        one using limited number of moves\
                    \n\t\trule 1: you can only move one disk at a time\
                    \n\t\trule 2: only disk of smaller value can be placed on the top\
                    \n\t\trule 3: every move is counted(even the invalid ones if attempted)\n";
        
        return;
    }
    // Print the values on the stacks 
    
    
    // return true if putting integer 'top' on stack 's' else false
    bool move_possible(stack<int> s, int top)
    {
        return true;
    } 
    // move a disc
    


};


int main ()
{
    //create a game
    Game* game = new Game();
    
    //start the game
    game->run();

    // before quiting wait until a key is pressed
    cin.get();
    return 0;
}
