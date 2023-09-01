cmake_minimum_required(VERSION 3.22)
project(3D-Image-Processing)

# Find ITK
find_package(ITK REQUIRED)
include(${ITK_USE_FILE})

# Find VTK
find_package(VTK REQUIRED)
include(${VTK_USE_FILE})

# Set Python version requirement
set(Python3_FIND_VERSION_MAJOR 3)
set(Python3_FIND_VERSION_MINOR 11)

add_executable(main src/main.cpp)
target_link_libraries(main ${ITK_LIBRARIES} ${VTK_LIBRARIES})


# UNINSTALL VTK :
# sudo make uninstall (in build directory : /opt/VTK-9.3.0.rc1/VTK-build)