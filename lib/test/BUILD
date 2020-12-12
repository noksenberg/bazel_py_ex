load("@py_deps//:requirements.bzl", "requirement")

py_test(
    main = "lib_test.py",
    name = "lib_test",
    srcs = ["lib_test.py"],
    deps = [
        "//lib:lib",
        requirement("pytest")
    ]
)