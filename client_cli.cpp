#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include "json.hpp"
using namespace std;


void print_intro();
void handle_commands(string command);


map <string, string> json = json_to_map("config.json");


int main(int argc, char *argv[])
{
	print_intro();
	string command;
	while (true)
	{
		cout << "> ";
		getline(cin, command);
		handle_commands(command);
	}
	return 0;
}


void print_intro()
{
	cout << "\n\t 111   1   1    1    11111" << endl
		<< "\t11     11111   1 1     1" << endl
		<< "\t11  1  1   1  11111    1" << endl
		<< "\t 111   1   1  1   1    1\n" << endl
		<< "\t\tname: " << json["name"] << endl
		<< "\t\tip: " << json["ip"] << endl
		<< "\t\tport: " << json["port"] << endl
		<< "\t\tkey: " << json["key"] << endl
		<< "\n\ttype 'help' for get manual\n" << endl;
}


void reload()
{
	system("clear");
	map_to_json("config.json", json);
	print_intro();
}


void handle_commands(string command)
{
	if (command == "set_name")
	{
		cout << "Enter your name > ";
		cin >> json["name"];
		reload();
	}
	else if (command == "set_key")
	{
		cout << "Enter your key > ";
		cin >> json["key"];
		reload();
	}
	else if (command == "set_ip")
	{
		cout << "Enter server ip > ";
		cin >> json["ip"];
		reload();
	}
	else if (command == "set_port")
	{
		cout << "Enter server port > ";
		cin >> json["port"];
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
	else if (command == "connect") { system("python3 socket_client.py"); }
	else if (command == "exit") { exit(0); }
	else if (command == "clear") { reload(); }
	else if (command == "") { }
	else { cout << "Non valid command" << endl; }
}
