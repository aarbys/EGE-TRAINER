// #include <iostream>
#include <fstream>
#include <string>
#include <ctime>
#include <random>
#include <vector>

using namespace std;

int main()
{
	std::ifstream conditions_file("conditions.txt");
	int MOP, columns, max_value;
	conditions_file >> MOP >> columns >> max_value;
	conditions_file.close();
	std::ofstream file_a("27_A.txt"); std::ofstream file_b("27_B.txt");

	std::minstd_rand gen(time(NULL));
	std::uniform_int_distribution<int> number_distribution(20, 1000);
	std::uniform_int_distribution<int> amountA_dist(150, 9000);
	std::uniform_int_distribution<long> amountB_dist(1000000, 10000000);
	int amount_a = amountA_dist(gen);
	long amount_b = amountB_dist(gen);
	std::string MOPFirstString = "";
	std::vector<std::pair<int, int>> MOPArray;
	std::string x = "";
	for (int i = 0; i < 2; i++)
	{
		if (MOP != 0)
		{
			std::uniform_int_distribution<int> prev_dist(1, 20);
			int prev = prev_dist(gen);
			if (i == 0)
			{
				int j = 0;
				while (j < amount_a)
				{
					MOPArray.push_back(std::pair<int, int>(prev, number_distribution(gen)));
					prev += prev_dist(gen);
					j++;
				}
			}
			else if (i == 1)
			{
				long j = 0;
				while (j < amount_b)
				{
					MOPArray.push_back(std::pair<int, int>(prev, number_distribution(gen)));
					prev += prev_dist(gen);
					j++;
				}
			}
			if (MOP == 2)
			{
				if (i == 0)
				{
					MOPFirstString = std::to_string(amount_a) + ' ' + std::to_string(MOPArray.back().first + number_distribution(gen)) + ' ' + std::to_string(int(amount_a / number_distribution(gen))) + '\n';
					for (std::pair<int, int> a : MOPArray)
						x += std::to_string(a.first) + ' ' + std::to_string(a.second) + '\n';
					x = MOPFirstString + x;
				}
				else if (i == 1)
				{
					MOPFirstString = std::to_string(amount_b) + ' ' + std::to_string(MOPArray.back().first + number_distribution(gen)) + ' ' + std::to_string(long(amount_b / number_distribution(gen))) + '\n';
					for (std::pair<int, int> a : MOPArray)
						x += std::to_string(a.first) + ' ' + std::to_string(a.second) + '\n';
					x = MOPFirstString + x;
				}
				MOPArray.clear();
			}
			else if (MOP == 1)
			{
				if (i == 0)
				{
					for (std::pair<int, int> a : MOPArray)
						x += std::to_string(a.first) + ' ' + std::to_string(a.second) + '\n';
					MOPFirstString = std::to_string(amount_a) + '\n';
					x = MOPFirstString + x;
				}
				else if (i == 1)
				{
					for (std::pair<int, int> a : MOPArray)
						x += std::to_string(a.first) + ' ' + std::to_string(a.second) + '\n';
					MOPFirstString = std::to_string(amount_b) + '\n';
					x = MOPFirstString + x;
				}
				MOPArray.clear();				
			}
		}
		else if (columns != 0)
		{
			if (i == 0)
			{
				x += std::to_string(amount_a) + '\n';
				int j = 0;
				while (j < amount_a)
				{
					std::string str = "";
					for (int k = 0; k < columns; k++)
						str += std::to_string(number_distribution(gen)) + ' ';
					x += str + '\n';
					j++;
				}
			}
			else if (i == 1)
			{
				x += std::to_string(amount_b) + '\n';
				long j = 0;
				while (j < amount_b)
				{
					std::string str = "";
					for (int k = 0; k < columns; k++)
						str += std::to_string(number_distribution(gen)) + ' ';
					x += str + '\n';
					j++;
				}
			}
		}
		else if (max_value != 0)
		{
			std::uniform_int_distribution<int> max_dist(1, max_value);
			if (i == 0)
			{
				x += std::to_string(amount_a) + '\n';
				int j = 0;
				while (j < amount_a)
				{
					x += std::to_string(max_dist(gen)) + '\n';
					j++;
				}
			}
			else if (i == 1)
			{
				x += std::to_string(amount_b) + '\n';
				long j = 0;
				while (j < amount_b)
				{
					x += std::to_string(max_dist(gen)) + '\n';
					j++;
				}
			}
		}
		if (i == 0)
		{
			file_a << x;
			file_a.close();
			x = "";
		}
		else if (i == 1)
		{
			file_b << x;
			file_b.close();
			x = "";
		}
	}
	return 0;
}
