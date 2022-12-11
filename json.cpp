#include <fstream>
#include <string>
#include <map>
using namespace std;


string __read_json(string filename)
{
	string json_str;
	char symbol;
	ifstream file (filename);
	while ( file )
	{
		symbol = file.get();
		json_str += symbol;
	}
	file.close();
	return json_str;
}


void map_to_json(string filename, map <string, string> json)
{
	string json_str;
	map <string, string> :: iterator it = json.begin();
	json_str += "{ ";
	for (int i = 0; it != json.end(); it++, i++)
	{
		if (i < 3)
			json_str += "\"" + it->first + "\"" + " : " + "\"" + it->second + "\"" + ", ";
		else
			json_str += "\"" + it->first + "\"" + " : " + "\"" + it->second + "\"";
	}
	json_str += " }\n";
	FILE *file = fopen(filename.c_str(), "w+");
	fwrite(json_str.c_str(), 1, json_str.size(), file);
	fclose(file);
}


map <string, string> json_to_map(string filename)
{
	string json_str = __read_json(filename);
	map <string, string> json;
	string key, value;
	bool begin = false, is_key = false;
	char symbol;

	for (char symbol : json_str)
	{
		if (begin)
		{
			if (symbol == '"')
			{
				begin = false;
				if (key.size() > 0 and value.size() > 0)
				{
					json[key] = value;
					key.clear();
					value.clear();
				}
				continue;
			}
			if (is_key)
				key += symbol;
			else
				value += symbol;
		}
		else if (symbol == '"')
		{
			if (is_key)
				is_key = false;
			else
				is_key = true;
			begin = true;
		}
		else
			continue;
	}
	return json;
}
