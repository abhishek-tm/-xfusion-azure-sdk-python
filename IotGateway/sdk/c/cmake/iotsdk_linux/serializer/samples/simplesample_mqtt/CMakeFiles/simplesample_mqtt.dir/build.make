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
include serializer/samples/simplesample_mqtt/CMakeFiles/simplesample_mqtt.dir/depend.make

# Include the progress variables for this target.
include serializer/samples/simplesample_mqtt/CMakeFiles/simplesample_mqtt.dir/progress.make

# Include the compile flags for this target's objects.
include serializer/samples/simplesample_mqtt/CMakeFiles/simplesample_mqtt.dir/flags.make

serializer/samples/simplesample_mqtt/CMakeFiles/simplesample_mqtt.dir/simplesample_mqtt.c.o: serializer/samples/simplesample_mqtt/CMakeFiles/simplesample_mqtt.dir/flags.make
serializer/samples/simplesample_mqtt/CMakeFiles/simplesample_mqtt.dir/simplesample_mqtt.c.o: ../../serializer/samples/simplesample_mqtt/simplesample_mqtt.c
	$(CMAKE_COMMAND) -E cmake_progress_report /home/pcone/Desktop/azure-iot-sdk-python/c/cmake/iotsdk_linux/CMakeFiles $(CMAKE_PROGRESS_1)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Building C object serializer/samples/simplesample_mqtt/CMakeFiles/simplesample_mqtt.dir/simplesample_mqtt.c.o"
	cd /home/pcone/Desktop/azure-iot-sdk-python/c/cmake/iotsdk_linux/serializer/samples/simplesample_mqtt && /usr/bin/cc  $(C_DEFINES) $(C_FLAGS) -o CMakeFiles/simplesample_mqtt.dir/simplesample_mqtt.c.o   -c /home/pcone/Desktop/azure-iot-sdk-python/c/serializer/samples/simplesample_mqtt/simplesample_mqtt.c

serializer/samples/simplesample_mqtt/CMakeFiles/simplesample_mqtt.dir/simplesample_mqtt.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/simplesample_mqtt.dir/simplesample_mqtt.c.i"
	cd /home/pcone/Desktop/azure-iot-sdk-python/c/cmake/iotsdk_linux/serializer/samples/simplesample_mqtt && /usr/bin/cc  $(C_DEFINES) $(C_FLAGS) -E /home/pcone/Desktop/azure-iot-sdk-python/c/serializer/samples/simplesample_mqtt/simplesample_mqtt.c > CMakeFiles/simplesample_mqtt.dir/simplesample_mqtt.c.i

serializer/samples/simplesample_mqtt/CMakeFiles/simplesample_mqtt.dir/simplesample_mqtt.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/simplesample_mqtt.dir/simplesample_mqtt.c.s"
	cd /home/pcone/Desktop/azure-iot-sdk-python/c/cmake/iotsdk_linux/serializer/samples/simplesample_mqtt && /usr/bin/cc  $(C_DEFINES) $(C_FLAGS) -S /home/pcone/Desktop/azure-iot-sdk-python/c/serializer/samples/simplesample_mqtt/simplesample_mqtt.c -o CMakeFiles/simplesample_mqtt.dir/simplesample_mqtt.c.s

serializer/samples/simplesample_mqtt/CMakeFiles/simplesample_mqtt.dir/simplesample_mqtt.c.o.requires:
.PHONY : serializer/samples/simplesample_mqtt/CMakeFiles/simplesample_mqtt.dir/simplesample_mqtt.c.o.requires

serializer/samples/simplesample_mqtt/CMakeFiles/simplesample_mqtt.dir/simplesample_mqtt.c.o.provides: serializer/samples/simplesample_mqtt/CMakeFiles/simplesample_mqtt.dir/simplesample_mqtt.c.o.requires
	$(MAKE) -f serializer/samples/simplesample_mqtt/CMakeFiles/simplesample_mqtt.dir/build.make serializer/samples/simplesample_mqtt/CMakeFiles/simplesample_mqtt.dir/simplesample_mqtt.c.o.provides.build
.PHONY : serializer/samples/simplesample_mqtt/CMakeFiles/simplesample_mqtt.dir/simplesample_mqtt.c.o.provides

serializer/samples/simplesample_mqtt/CMakeFiles/simplesample_mqtt.dir/simplesample_mqtt.c.o.provides.build: serializer/samples/simplesample_mqtt/CMakeFiles/simplesample_mqtt.dir/simplesample_mqtt.c.o

serializer/samples/simplesample_mqtt/CMakeFiles/simplesample_mqtt.dir/linux/main.c.o: serializer/samples/simplesample_mqtt/CMakeFiles/simplesample_mqtt.dir/flags.make
serializer/samples/simplesample_mqtt/CMakeFiles/simplesample_mqtt.dir/linux/main.c.o: ../../serializer/samples/simplesample_mqtt/linux/main.c
	$(CMAKE_COMMAND) -E cmake_progress_report /home/pcone/Desktop/azure-iot-sdk-python/c/cmake/iotsdk_linux/CMakeFiles $(CMAKE_PROGRESS_2)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Building C object serializer/samples/simplesample_mqtt/CMakeFiles/simplesample_mqtt.dir/linux/main.c.o"
	cd /home/pcone/Desktop/azure-iot-sdk-python/c/cmake/iotsdk_linux/serializer/samples/simplesample_mqtt && /usr/bin/cc  $(C_DEFINES) $(C_FLAGS) -o CMakeFiles/simplesample_mqtt.dir/linux/main.c.o   -c /home/pcone/Desktop/azure-iot-sdk-python/c/serializer/samples/simplesample_mqtt/linux/main.c

serializer/samples/simplesample_mqtt/CMakeFiles/simplesample_mqtt.dir/linux/main.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/simplesample_mqtt.dir/linux/main.c.i"
	cd /home/pcone/Desktop/azure-iot-sdk-python/c/cmake/iotsdk_linux/serializer/samples/simplesample_mqtt && /usr/bin/cc  $(C_DEFINES) $(C_FLAGS) -E /home/pcone/Desktop/azure-iot-sdk-python/c/serializer/samples/simplesample_mqtt/linux/main.c > CMakeFiles/simplesample_mqtt.dir/linux/main.c.i

serializer/samples/simplesample_mqtt/CMakeFiles/simplesample_mqtt.dir/linux/main.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/simplesample_mqtt.dir/linux/main.c.s"
	cd /home/pcone/Desktop/azure-iot-sdk-python/c/cmake/iotsdk_linux/serializer/samples/simplesample_mqtt && /usr/bin/cc  $(C_DEFINES) $(C_FLAGS) -S /home/pcone/Desktop/azure-iot-sdk-python/c/serializer/samples/simplesample_mqtt/linux/main.c -o CMakeFiles/simplesample_mqtt.dir/linux/main.c.s

serializer/samples/simplesample_mqtt/CMakeFiles/simplesample_mqtt.dir/linux/main.c.o.requires:
.PHONY : serializer/samples/simplesample_mqtt/CMakeFiles/simplesample_mqtt.dir/linux/main.c.o.requires

serializer/samples/simplesample_mqtt/CMakeFiles/simplesample_mqtt.dir/linux/main.c.o.provides: serializer/samples/simplesample_mqtt/CMakeFiles/simplesample_mqtt.dir/linux/main.c.o.requires
	$(MAKE) -f serializer/samples/simplesample_mqtt/CMakeFiles/simplesample_mqtt.dir/build.make serializer/samples/simplesample_mqtt/CMakeFiles/simplesample_mqtt.dir/linux/main.c.o.provides.build
.PHONY : serializer/samples/simplesample_mqtt/CMakeFiles/simplesample_mqtt.dir/linux/main.c.o.provides

serializer/samples/simplesample_mqtt/CMakeFiles/simplesample_mqtt.dir/linux/main.c.o.provides.build: serializer/samples/simplesample_mqtt/CMakeFiles/simplesample_mqtt.dir/linux/main.c.o

# Object files for target simplesample_mqtt
simplesample_mqtt_OBJECTS = \
"CMakeFiles/simplesample_mqtt.dir/simplesample_mqtt.c.o" \
"CMakeFiles/simplesample_mqtt.dir/linux/main.c.o"

# External object files for target simplesample_mqtt
simplesample_mqtt_EXTERNAL_OBJECTS =

serializer/samples/simplesample_mqtt/simplesample_mqtt: serializer/samples/simplesample_mqtt/CMakeFiles/simplesample_mqtt.dir/simplesample_mqtt.c.o
serializer/samples/simplesample_mqtt/simplesample_mqtt: serializer/samples/simplesample_mqtt/CMakeFiles/simplesample_mqtt.dir/linux/main.c.o
serializer/samples/simplesample_mqtt/simplesample_mqtt: serializer/samples/simplesample_mqtt/CMakeFiles/simplesample_mqtt.dir/build.make
serializer/samples/simplesample_mqtt/simplesample_mqtt: iothub_client/libiothub_client_mqtt_transport.a
serializer/samples/simplesample_mqtt/simplesample_mqtt: serializer/libserializer.a
serializer/samples/simplesample_mqtt/simplesample_mqtt: iothub_client/libiothub_client.a
serializer/samples/simplesample_mqtt/simplesample_mqtt: umqtt/libumqtt.a
serializer/samples/simplesample_mqtt/simplesample_mqtt: c-utility/libaziotsharedutil.a
serializer/samples/simplesample_mqtt/simplesample_mqtt: /usr/lib/x86_64-linux-gnu/libssl.so
serializer/samples/simplesample_mqtt/simplesample_mqtt: /usr/lib/x86_64-linux-gnu/libcrypto.so
serializer/samples/simplesample_mqtt/simplesample_mqtt: serializer/samples/simplesample_mqtt/CMakeFiles/simplesample_mqtt.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --red --bold "Linking C executable simplesample_mqtt"
	cd /home/pcone/Desktop/azure-iot-sdk-python/c/cmake/iotsdk_linux/serializer/samples/simplesample_mqtt && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/simplesample_mqtt.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
serializer/samples/simplesample_mqtt/CMakeFiles/simplesample_mqtt.dir/build: serializer/samples/simplesample_mqtt/simplesample_mqtt
.PHONY : serializer/samples/simplesample_mqtt/CMakeFiles/simplesample_mqtt.dir/build

serializer/samples/simplesample_mqtt/CMakeFiles/simplesample_mqtt.dir/requires: serializer/samples/simplesample_mqtt/CMakeFiles/simplesample_mqtt.dir/simplesample_mqtt.c.o.requires
serializer/samples/simplesample_mqtt/CMakeFiles/simplesample_mqtt.dir/requires: serializer/samples/simplesample_mqtt/CMakeFiles/simplesample_mqtt.dir/linux/main.c.o.requires
.PHONY : serializer/samples/simplesample_mqtt/CMakeFiles/simplesample_mqtt.dir/requires

serializer/samples/simplesample_mqtt/CMakeFiles/simplesample_mqtt.dir/clean:
	cd /home/pcone/Desktop/azure-iot-sdk-python/c/cmake/iotsdk_linux/serializer/samples/simplesample_mqtt && $(CMAKE_COMMAND) -P CMakeFiles/simplesample_mqtt.dir/cmake_clean.cmake
.PHONY : serializer/samples/simplesample_mqtt/CMakeFiles/simplesample_mqtt.dir/clean

serializer/samples/simplesample_mqtt/CMakeFiles/simplesample_mqtt.dir/depend:
	cd /home/pcone/Desktop/azure-iot-sdk-python/c/cmake/iotsdk_linux && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/pcone/Desktop/azure-iot-sdk-python/c /home/pcone/Desktop/azure-iot-sdk-python/c/serializer/samples/simplesample_mqtt /home/pcone/Desktop/azure-iot-sdk-python/c/cmake/iotsdk_linux /home/pcone/Desktop/azure-iot-sdk-python/c/cmake/iotsdk_linux/serializer/samples/simplesample_mqtt /home/pcone/Desktop/azure-iot-sdk-python/c/cmake/iotsdk_linux/serializer/samples/simplesample_mqtt/CMakeFiles/simplesample_mqtt.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : serializer/samples/simplesample_mqtt/CMakeFiles/simplesample_mqtt.dir/depend

