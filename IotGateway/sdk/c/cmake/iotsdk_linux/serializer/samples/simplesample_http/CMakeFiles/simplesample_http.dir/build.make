# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 2.8

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list

# Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/pcone/Desktop/azure-iot-sdk-python/c

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/pcone/Desktop/azure-iot-sdk-python/c/cmake/iotsdk_linux

# Include any dependencies generated for this target.
include serializer/samples/simplesample_http/CMakeFiles/simplesample_http.dir/depend.make

# Include the progress variables for this target.
include serializer/samples/simplesample_http/CMakeFiles/simplesample_http.dir/progress.make

# Include the compile flags for this target's objects.
include serializer/samples/simplesample_http/CMakeFiles/simplesample_http.dir/flags.make

serializer/samples/simplesample_http/CMakeFiles/simplesample_http.dir/simplesample_http.c.o: serializer/samples/simplesample_http/CMakeFiles/simplesample_http.dir/flags.make
serializer/samples/simplesample_http/CMakeFiles/simplesample_http.dir/simplesample_http.c.o: ../../serializer/samples/simplesample_http/simplesample_http.c
	$(CMAKE_COMMAND) -E cmake_progress_report /home/pcone/Desktop/azure-iot-sdk-python/c/cmake/iotsdk_linux/CMakeFiles $(CMAKE_PROGRESS_1)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Building C object serializer/samples/simplesample_http/CMakeFiles/simplesample_http.dir/simplesample_http.c.o"
	cd /home/pcone/Desktop/azure-iot-sdk-python/c/cmake/iotsdk_linux/serializer/samples/simplesample_http && /usr/bin/cc  $(C_DEFINES) $(C_FLAGS) -o CMakeFiles/simplesample_http.dir/simplesample_http.c.o   -c /home/pcone/Desktop/azure-iot-sdk-python/c/serializer/samples/simplesample_http/simplesample_http.c

serializer/samples/simplesample_http/CMakeFiles/simplesample_http.dir/simplesample_http.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/simplesample_http.dir/simplesample_http.c.i"
	cd /home/pcone/Desktop/azure-iot-sdk-python/c/cmake/iotsdk_linux/serializer/samples/simplesample_http && /usr/bin/cc  $(C_DEFINES) $(C_FLAGS) -E /home/pcone/Desktop/azure-iot-sdk-python/c/serializer/samples/simplesample_http/simplesample_http.c > CMakeFiles/simplesample_http.dir/simplesample_http.c.i

serializer/samples/simplesample_http/CMakeFiles/simplesample_http.dir/simplesample_http.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/simplesample_http.dir/simplesample_http.c.s"
	cd /home/pcone/Desktop/azure-iot-sdk-python/c/cmake/iotsdk_linux/serializer/samples/simplesample_http && /usr/bin/cc  $(C_DEFINES) $(C_FLAGS) -S /home/pcone/Desktop/azure-iot-sdk-python/c/serializer/samples/simplesample_http/simplesample_http.c -o CMakeFiles/simplesample_http.dir/simplesample_http.c.s

serializer/samples/simplesample_http/CMakeFiles/simplesample_http.dir/simplesample_http.c.o.requires:
.PHONY : serializer/samples/simplesample_http/CMakeFiles/simplesample_http.dir/simplesample_http.c.o.requires

serializer/samples/simplesample_http/CMakeFiles/simplesample_http.dir/simplesample_http.c.o.provides: serializer/samples/simplesample_http/CMakeFiles/simplesample_http.dir/simplesample_http.c.o.requires
	$(MAKE) -f serializer/samples/simplesample_http/CMakeFiles/simplesample_http.dir/build.make serializer/samples/simplesample_http/CMakeFiles/simplesample_http.dir/simplesample_http.c.o.provides.build
.PHONY : serializer/samples/simplesample_http/CMakeFiles/simplesample_http.dir/simplesample_http.c.o.provides

serializer/samples/simplesample_http/CMakeFiles/simplesample_http.dir/simplesample_http.c.o.provides.build: serializer/samples/simplesample_http/CMakeFiles/simplesample_http.dir/simplesample_http.c.o

serializer/samples/simplesample_http/CMakeFiles/simplesample_http.dir/linux/main.c.o: serializer/samples/simplesample_http/CMakeFiles/simplesample_http.dir/flags.make
serializer/samples/simplesample_http/CMakeFiles/simplesample_http.dir/linux/main.c.o: ../../serializer/samples/simplesample_http/linux/main.c
	$(CMAKE_COMMAND) -E cmake_progress_report /home/pcone/Desktop/azure-iot-sdk-python/c/cmake/iotsdk_linux/CMakeFiles $(CMAKE_PROGRESS_2)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Building C object serializer/samples/simplesample_http/CMakeFiles/simplesample_http.dir/linux/main.c.o"
	cd /home/pcone/Desktop/azure-iot-sdk-python/c/cmake/iotsdk_linux/serializer/samples/simplesample_http && /usr/bin/cc  $(C_DEFINES) $(C_FLAGS) -o CMakeFiles/simplesample_http.dir/linux/main.c.o   -c /home/pcone/Desktop/azure-iot-sdk-python/c/serializer/samples/simplesample_http/linux/main.c

serializer/samples/simplesample_http/CMakeFiles/simplesample_http.dir/linux/main.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/simplesample_http.dir/linux/main.c.i"
	cd /home/pcone/Desktop/azure-iot-sdk-python/c/cmake/iotsdk_linux/serializer/samples/simplesample_http && /usr/bin/cc  $(C_DEFINES) $(C_FLAGS) -E /home/pcone/Desktop/azure-iot-sdk-python/c/serializer/samples/simplesample_http/linux/main.c > CMakeFiles/simplesample_http.dir/linux/main.c.i

serializer/samples/simplesample_http/CMakeFiles/simplesample_http.dir/linux/main.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/simplesample_http.dir/linux/main.c.s"
	cd /home/pcone/Desktop/azure-iot-sdk-python/c/cmake/iotsdk_linux/serializer/samples/simplesample_http && /usr/bin/cc  $(C_DEFINES) $(C_FLAGS) -S /home/pcone/Desktop/azure-iot-sdk-python/c/serializer/samples/simplesample_http/linux/main.c -o CMakeFiles/simplesample_http.dir/linux/main.c.s

serializer/samples/simplesample_http/CMakeFiles/simplesample_http.dir/linux/main.c.o.requires:
.PHONY : serializer/samples/simplesample_http/CMakeFiles/simplesample_http.dir/linux/main.c.o.requires

serializer/samples/simplesample_http/CMakeFiles/simplesample_http.dir/linux/main.c.o.provides: serializer/samples/simplesample_http/CMakeFiles/simplesample_http.dir/linux/main.c.o.requires
	$(MAKE) -f serializer/samples/simplesample_http/CMakeFiles/simplesample_http.dir/build.make serializer/samples/simplesample_http/CMakeFiles/simplesample_http.dir/linux/main.c.o.provides.build
.PHONY : serializer/samples/simplesample_http/CMakeFiles/simplesample_http.dir/linux/main.c.o.provides

serializer/samples/simplesample_http/CMakeFiles/simplesample_http.dir/linux/main.c.o.provides.build: serializer/samples/simplesample_http/CMakeFiles/simplesample_http.dir/linux/main.c.o

# Object files for target simplesample_http
simplesample_http_OBJECTS = \
"CMakeFiles/simplesample_http.dir/simplesample_http.c.o" \
"CMakeFiles/simplesample_http.dir/linux/main.c.o"

# External object files for target simplesample_http
simplesample_http_EXTERNAL_OBJECTS =

serializer/samples/simplesample_http/simplesample_http: serializer/samples/simplesample_http/CMakeFiles/simplesample_http.dir/simplesample_http.c.o
serializer/samples/simplesample_http/simplesample_http: serializer/samples/simplesample_http/CMakeFiles/simplesample_http.dir/linux/main.c.o
serializer/samples/simplesample_http/simplesample_http: serializer/samples/simplesample_http/CMakeFiles/simplesample_http.dir/build.make
serializer/samples/simplesample_http/simplesample_http: serializer/libserializer.a
serializer/samples/simplesample_http/simplesample_http: iothub_client/libiothub_client.a
serializer/samples/simplesample_http/simplesample_http: iothub_client/libiothub_client_http_transport.a
serializer/samples/simplesample_http/simplesample_http: c-utility/libaziotsharedutil.a
serializer/samples/simplesample_http/simplesample_http: /usr/lib/x86_64-linux-gnu/libssl.so
serializer/samples/simplesample_http/simplesample_http: /usr/lib/x86_64-linux-gnu/libcrypto.so
serializer/samples/simplesample_http/simplesample_http: serializer/samples/simplesample_http/CMakeFiles/simplesample_http.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --red --bold "Linking C executable simplesample_http"
	cd /home/pcone/Desktop/azure-iot-sdk-python/c/cmake/iotsdk_linux/serializer/samples/simplesample_http && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/simplesample_http.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
serializer/samples/simplesample_http/CMakeFiles/simplesample_http.dir/build: serializer/samples/simplesample_http/simplesample_http
.PHONY : serializer/samples/simplesample_http/CMakeFiles/simplesample_http.dir/build

serializer/samples/simplesample_http/CMakeFiles/simplesample_http.dir/requires: serializer/samples/simplesample_http/CMakeFiles/simplesample_http.dir/simplesample_http.c.o.requires
serializer/samples/simplesample_http/CMakeFiles/simplesample_http.dir/requires: serializer/samples/simplesample_http/CMakeFiles/simplesample_http.dir/linux/main.c.o.requires
.PHONY : serializer/samples/simplesample_http/CMakeFiles/simplesample_http.dir/requires

serializer/samples/simplesample_http/CMakeFiles/simplesample_http.dir/clean:
	cd /home/pcone/Desktop/azure-iot-sdk-python/c/cmake/iotsdk_linux/serializer/samples/simplesample_http && $(CMAKE_COMMAND) -P CMakeFiles/simplesample_http.dir/cmake_clean.cmake
.PHONY : serializer/samples/simplesample_http/CMakeFiles/simplesample_http.dir/clean

serializer/samples/simplesample_http/CMakeFiles/simplesample_http.dir/depend:
	cd /home/pcone/Desktop/azure-iot-sdk-python/c/cmake/iotsdk_linux && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/pcone/Desktop/azure-iot-sdk-python/c /home/pcone/Desktop/azure-iot-sdk-python/c/serializer/samples/simplesample_http /home/pcone/Desktop/azure-iot-sdk-python/c/cmake/iotsdk_linux /home/pcone/Desktop/azure-iot-sdk-python/c/cmake/iotsdk_linux/serializer/samples/simplesample_http /home/pcone/Desktop/azure-iot-sdk-python/c/cmake/iotsdk_linux/serializer/samples/simplesample_http/CMakeFiles/simplesample_http.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : serializer/samples/simplesample_http/CMakeFiles/simplesample_http.dir/depend

