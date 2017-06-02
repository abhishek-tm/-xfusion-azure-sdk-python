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
include serializer/samples/remote_monitoring/CMakeFiles/remote_monitoring.dir/depend.make

# Include the progress variables for this target.
include serializer/samples/remote_monitoring/CMakeFiles/remote_monitoring.dir/progress.make

# Include the compile flags for this target's objects.
include serializer/samples/remote_monitoring/CMakeFiles/remote_monitoring.dir/flags.make

serializer/samples/remote_monitoring/CMakeFiles/remote_monitoring.dir/remote_monitoring.c.o: serializer/samples/remote_monitoring/CMakeFiles/remote_monitoring.dir/flags.make
serializer/samples/remote_monitoring/CMakeFiles/remote_monitoring.dir/remote_monitoring.c.o: ../../serializer/samples/remote_monitoring/remote_monitoring.c
	$(CMAKE_COMMAND) -E cmake_progress_report /home/pcone/Desktop/azure-iot-sdk-python/c/cmake/iotsdk_linux/CMakeFiles $(CMAKE_PROGRESS_1)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Building C object serializer/samples/remote_monitoring/CMakeFiles/remote_monitoring.dir/remote_monitoring.c.o"
	cd /home/pcone/Desktop/azure-iot-sdk-python/c/cmake/iotsdk_linux/serializer/samples/remote_monitoring && /usr/bin/cc  $(C_DEFINES) $(C_FLAGS) -o CMakeFiles/remote_monitoring.dir/remote_monitoring.c.o   -c /home/pcone/Desktop/azure-iot-sdk-python/c/serializer/samples/remote_monitoring/remote_monitoring.c

serializer/samples/remote_monitoring/CMakeFiles/remote_monitoring.dir/remote_monitoring.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/remote_monitoring.dir/remote_monitoring.c.i"
	cd /home/pcone/Desktop/azure-iot-sdk-python/c/cmake/iotsdk_linux/serializer/samples/remote_monitoring && /usr/bin/cc  $(C_DEFINES) $(C_FLAGS) -E /home/pcone/Desktop/azure-iot-sdk-python/c/serializer/samples/remote_monitoring/remote_monitoring.c > CMakeFiles/remote_monitoring.dir/remote_monitoring.c.i

serializer/samples/remote_monitoring/CMakeFiles/remote_monitoring.dir/remote_monitoring.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/remote_monitoring.dir/remote_monitoring.c.s"
	cd /home/pcone/Desktop/azure-iot-sdk-python/c/cmake/iotsdk_linux/serializer/samples/remote_monitoring && /usr/bin/cc  $(C_DEFINES) $(C_FLAGS) -S /home/pcone/Desktop/azure-iot-sdk-python/c/serializer/samples/remote_monitoring/remote_monitoring.c -o CMakeFiles/remote_monitoring.dir/remote_monitoring.c.s

serializer/samples/remote_monitoring/CMakeFiles/remote_monitoring.dir/remote_monitoring.c.o.requires:
.PHONY : serializer/samples/remote_monitoring/CMakeFiles/remote_monitoring.dir/remote_monitoring.c.o.requires

serializer/samples/remote_monitoring/CMakeFiles/remote_monitoring.dir/remote_monitoring.c.o.provides: serializer/samples/remote_monitoring/CMakeFiles/remote_monitoring.dir/remote_monitoring.c.o.requires
	$(MAKE) -f serializer/samples/remote_monitoring/CMakeFiles/remote_monitoring.dir/build.make serializer/samples/remote_monitoring/CMakeFiles/remote_monitoring.dir/remote_monitoring.c.o.provides.build
.PHONY : serializer/samples/remote_monitoring/CMakeFiles/remote_monitoring.dir/remote_monitoring.c.o.provides

serializer/samples/remote_monitoring/CMakeFiles/remote_monitoring.dir/remote_monitoring.c.o.provides.build: serializer/samples/remote_monitoring/CMakeFiles/remote_monitoring.dir/remote_monitoring.c.o

# Object files for target remote_monitoring
remote_monitoring_OBJECTS = \
"CMakeFiles/remote_monitoring.dir/remote_monitoring.c.o"

# External object files for target remote_monitoring
remote_monitoring_EXTERNAL_OBJECTS =

serializer/samples/remote_monitoring/remote_monitoring: serializer/samples/remote_monitoring/CMakeFiles/remote_monitoring.dir/remote_monitoring.c.o
serializer/samples/remote_monitoring/remote_monitoring: serializer/samples/remote_monitoring/CMakeFiles/remote_monitoring.dir/build.make
serializer/samples/remote_monitoring/remote_monitoring: serializer/libserializer.a
serializer/samples/remote_monitoring/remote_monitoring: iothub_client/libiothub_client.a
serializer/samples/remote_monitoring/remote_monitoring: iothub_client/libiothub_client_amqp_transport.a
serializer/samples/remote_monitoring/remote_monitoring: c-utility/libaziotsharedutil.a
serializer/samples/remote_monitoring/remote_monitoring: uamqp/libuamqp.a
serializer/samples/remote_monitoring/remote_monitoring: c-utility/libaziotsharedutil.a
serializer/samples/remote_monitoring/remote_monitoring: /usr/lib/x86_64-linux-gnu/libssl.so
serializer/samples/remote_monitoring/remote_monitoring: /usr/lib/x86_64-linux-gnu/libcrypto.so
serializer/samples/remote_monitoring/remote_monitoring: serializer/samples/remote_monitoring/CMakeFiles/remote_monitoring.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --red --bold "Linking C executable remote_monitoring"
	cd /home/pcone/Desktop/azure-iot-sdk-python/c/cmake/iotsdk_linux/serializer/samples/remote_monitoring && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/remote_monitoring.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
serializer/samples/remote_monitoring/CMakeFiles/remote_monitoring.dir/build: serializer/samples/remote_monitoring/remote_monitoring
.PHONY : serializer/samples/remote_monitoring/CMakeFiles/remote_monitoring.dir/build

serializer/samples/remote_monitoring/CMakeFiles/remote_monitoring.dir/requires: serializer/samples/remote_monitoring/CMakeFiles/remote_monitoring.dir/remote_monitoring.c.o.requires
.PHONY : serializer/samples/remote_monitoring/CMakeFiles/remote_monitoring.dir/requires

serializer/samples/remote_monitoring/CMakeFiles/remote_monitoring.dir/clean:
	cd /home/pcone/Desktop/azure-iot-sdk-python/c/cmake/iotsdk_linux/serializer/samples/remote_monitoring && $(CMAKE_COMMAND) -P CMakeFiles/remote_monitoring.dir/cmake_clean.cmake
.PHONY : serializer/samples/remote_monitoring/CMakeFiles/remote_monitoring.dir/clean

serializer/samples/remote_monitoring/CMakeFiles/remote_monitoring.dir/depend:
	cd /home/pcone/Desktop/azure-iot-sdk-python/c/cmake/iotsdk_linux && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/pcone/Desktop/azure-iot-sdk-python/c /home/pcone/Desktop/azure-iot-sdk-python/c/serializer/samples/remote_monitoring /home/pcone/Desktop/azure-iot-sdk-python/c/cmake/iotsdk_linux /home/pcone/Desktop/azure-iot-sdk-python/c/cmake/iotsdk_linux/serializer/samples/remote_monitoring /home/pcone/Desktop/azure-iot-sdk-python/c/cmake/iotsdk_linux/serializer/samples/remote_monitoring/CMakeFiles/remote_monitoring.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : serializer/samples/remote_monitoring/CMakeFiles/remote_monitoring.dir/depend

