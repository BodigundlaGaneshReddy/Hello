cmake_minimum_required(VERSION 3.12)
project(MyApp)
 
# Locate and configure Google Test
find_package(GTest REQUIRED)
include_directories(${GTEST_INCLUDE_DIRS})
 
# Create an executable for the main program
add_executable(main main.cpp)
 
# Create an executable for the tests
add_executable(tests test.cpp)
 
# Link the main program with Google Test
target_link_libraries(main PRIVATE ${GTEST_LIBRARIES} ${GTEST_MAIN_LIBRARIES})
 
# Link the tests with Google Test and the main program
target_link_libraries(tests PRIVATE ${GTEST_LIBRARIES} ${GTEST_MAIN_LIBRARIES})
 
# Optionally, you can enable C++11 features
target_compile_features(main PRIVATE cxx_std_11)
target_compile_features(tests PRIVATE cxx_std_11)