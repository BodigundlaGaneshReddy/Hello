cmake_minimum_required(VERSION 3.10)
project(HelloWorld)
 
# Set C++ standard to C++11
set(CMAKE_CXX_STANDARD 11)
 
# Add the executable for the main program
add_executable(main main.cpp)
 
# Add the executable for the tests
add_executable(tests test.cpp)
 
# Include Google Test
include(GoogleTest)
gtest_discover_tests(tests)
 
# Set up Cppcheck
find_program(CPPCHECK cppcheck)
if(CPPCHECK)
    set(CPPCHECK_COMMAND ${CPPCHECK} ARGS --project=cppcheck-config.txt --inline-suppr --quiet)
    add_custom_target(run-cppcheck ALL
        COMMAND ${CPPCHECK_COMMAND} ${CMAKE_SOURCE_DIR}/main.cpp
        COMMENT "Running Cppcheck on main.cpp"
    )
endif()
 
# Link Google Test
target_link_libraries(tests gtest gtest_main)
 
# Enable testing
enable_testing()
add_test(NAME HelloWorldTests COMMAND tests)