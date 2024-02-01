cmake_minimum_required(VERSION 3.10)
 
project(HelloWorld)
 
# Add the executable for the main program
add_executable(main main.cpp)
 
# Add the executable for the tests
add_executable(tests test.cpp)
 
# Include Google Test and link it with the tests
include(FetchContent)
FetchContent_Declare(
    googletest
GIT_REPOSITORY https://github.com/google/googletest.git
    GIT_TAG release-1.11.0
)
FetchContent_MakeAvailable(googletest)
target_link_libraries(tests gtest_main)
 
# Define a custom target for running tests
add_custom_target(run_tests COMMAND tests)