#include <iostream>
#include <string>
#include <fstream>

using namespace std;

string name = "user";
string ip = "0.0.0.0";
int port = 4444;
string key = "12345";


void print_intro();
void handle_commands(string command);


int main()
{
	print_intro();
	string command;
	while (true)
	{
		cout << "> ";
		cin >> command;
		handle_commands(command);
	}
	return 0;
}


void print_intro()
{
	cout << "\n\t 111   1   1    1    11111" << endl;
	cout << "\t11     11111   1 1     1" << endl;
	cout << "\t11  1  1   1  11111    1" << endl;
	cout << "\t 111   1   1  1   1    1\n" << endl;
	cout << "\t\tname: " << name << endl;
	cout << "\t\tip: " << ip << endl;
	cout << "\t\tport: " << port << endl;
	cout << "\t\tkey: " << key << endl;
	cout << "\n\ttype 'help' for get manual\n" << endl;
}


void reload()
{
	system("clear");
	print_intro();
}


void handle_commands(string command)
{
	if (command == "set_name")
	{
		cout << "Enter your name > ";
		cin >> name;
		reload();
	}
	else if (command == "set_key")
	{
		cout << "Enter your key > ";
		cin >> key;
		reload();
	}
	else if (command == "set_ip")
	{
		cout << "Enter server ip > ";
		cin >> ip;
		reload();
	}
	else if (command == "set_port")
	{
		cout << "Enter server port > ";
		cin >> port;
		reload();
	}
	else if (command == "help")
	{
		ifstream file ("help");
		char mychar;
		while ( file )
		{
			mychar = file.get();
			cout << mychar;
		}
		file.close();
	}
	else if (command == "connect") { cout << command << endl; }
	else if (command == "exit") { exit(0); }
	else if (command == "clear") { reload(); }
	else { cout << "Non valid command" << endl; }
}
