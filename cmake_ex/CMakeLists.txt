# Cmake version requirement
cmake_minimum_required(VERSION 2.6)

# Project information
Project (ex_math)

# reference directory
add_subdirectory(MyMathLib)
add_executable(ex_math src/main.cpp)

# linking library
target_link_libraries(ex_math PUBLIC MyMath)

# include
target_include_directories(ex_math PUBLIC "${PROJECT_BINARY_DIR}" "${PROJECT_SOURCE_DIR}/MyMathLib")

