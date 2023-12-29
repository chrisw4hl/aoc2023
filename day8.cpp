#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <unordered_map>
#include <utility>

int main(){
	std::ifstream myfile ("8.txt");
	std::string line;
	std::string dirs;
	std::string node;
	std::string fir;
	std::string sec;
	int i = 0;
	int dirlen;
	
	std::unordered_map<std::string, std::pair<std::string, std::string>> dict;

	getline(myfile, dirs);
	std::string cur = "AAA";

	while(getline(myfile, line)){
		std::istringstream iss(line);
		getline(iss, node, '=');
		node = node.substr(0,node.size()-1);
		getline(iss, fir, ',');
		dict[node].first = fir.substr(2,fir.size()-2);
		getline(iss, sec);
		dict[node].second = sec.substr(1,sec.size()-2);
	}

	dirlen = dirs.length();
	std::istringstream dss(dirs);
	
	int count = 0;
	char c = 'Z';

	dss >> c;
	while(cur != "ZZZ"){
		c = dirs[i];
		if (c == 'L'){
			cur = dict[cur].first;
			count++;
		} else if (c == 'R'){
			cur = dict[cur].second;
			count++;
		} else{
			std::cout << "error" << std::endl;
		}
		if (cur == "ZZZ"){
			std::cout << count << std::endl;
			break;
		}

		if (i == 0){
			i++; 
		}else if ((i % (dirlen-1)) == 0){
			i=0;
		}else {
			i++;
		}
	}

	myfile.close();
	return 0;
}
	
