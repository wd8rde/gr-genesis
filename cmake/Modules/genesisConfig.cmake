INCLUDE(FindPkgConfig)
PKG_CHECK_MODULES(PC_GENESIS genesis)

FIND_PATH(
    GENESIS_INCLUDE_DIRS
    NAMES genesis/api.h
    HINTS $ENV{GENESIS_DIR}/include
        ${PC_GENESIS_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    GENESIS_LIBRARIES
    NAMES gnuradio-genesis
    HINTS $ENV{GENESIS_DIR}/lib
        ${PC_GENESIS_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
)

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(GENESIS DEFAULT_MSG GENESIS_LIBRARIES GENESIS_INCLUDE_DIRS)
MARK_AS_ADVANCED(GENESIS_LIBRARIES GENESIS_INCLUDE_DIRS)

