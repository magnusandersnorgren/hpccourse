#include <iostream>
#include<vector>
#include <boost/python.hpp>

char const* greet()
{
	return "hello hpc course";
}

class variants {
	
	private:
		std::vector<int> container;

	public: 

		void print_container(){
			std::cout << "{" << std::endl;
			for (auto i : container) {
				std::cout << i << std::endl;
			}
			std::cout << "}" << std::endl;
		}

		void add_position(int variant){
			container.push_back(variant);
		}

		boost::python::tuple maximum_stretch(int length){
			int tmpstart, tmplast, current_max_start, current_max_end, current_max_len;
			current_max_start = container[0];
			current_max_end = container[0];
			current_max_len = 0;			
			tmpstart = container[0];
			tmplast = container[0];

			for (auto i : container) {
				auto len = i-tmplast;
				if(len > length){
					len = tmplast-tmpstart;
					if(len > current_max_len){
						current_max_start = tmpstart;
						current_max_end = tmplast;
						current_max_len = len;
					}
					tmpstart = i;
				}
				tmplast = i;
			}
			
			//check last
			auto len = tmplast-tmpstart;
			if(len > current_max_len){
				current_max_start = tmpstart;
				current_max_end = tmplast;
			}
			

			return boost::python::make_tuple(current_max_start,current_max_end);
		}
};

BOOST_PYTHON_MODULE(hello_ext)
{
	using namespace boost::python;
	def("greet", greet);
	
	class_<variants> ("variants")
		.def("add_position", &variants::add_position)
		.def("maximum_stretch", &variants::maximum_stretch)
		.def("print_container", &variants::print_container)
		;
}
