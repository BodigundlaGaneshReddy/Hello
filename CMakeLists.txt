cmake_minimum_required(VERSION 3.12)
project(HelloWorldProject)
 
# C++ standard version
set(CMAKE_CXX_STANDARD 11)
 
# Add the executable
add_executable(hello_world main.cpp)
 
# Cppcheck integration
find_program(CPPCHECK_EXECUTABLE NAMES cppcheck)
if(CPPCHECK_EXECUTABLE)
    list(APPEND CMAKE_CXX_CPPCHECK "${CPPCHECK_EXECUTABLE};--std=c++11;--enable=all")
else()
    message(WARNING "Cppcheck not found. Static code analysis will be disabled.")
endif()
 
# Google Test setup (download and build)
include(FetchContent)
FetchContent_Declare(
    googletest
GIT_REPOSITORY https://github.com/google/googletest.git
    GIT_TAG release-1.10.0
)
FetchContent_MakeAvailable(googletest)
 
# Add the test executable
add_executable(tests test.cpp)
target_link_libraries(tests gtest gtest_main)
 
# Enable testing
include(GoogleTest)
gtest_discover_tests(tests)
