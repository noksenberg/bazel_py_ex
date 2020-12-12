load("@py_deps//:requirements.bzl", "requirement")

py_binary(
    name = "main",
    srcs = ["main.py"],
    deps = [
        "//lib:lib",
        requirement("fastapi"),
        requirement("uvicorn")
    ],
)
