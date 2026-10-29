// swift-tools-version: 6.0
import PackageDescription

let package = Package(
    name: "lb3",
    platforms: [.macOS(.v13)],
    products: [
        .executable(name: "lb3", targets: ["lb3"])
    ],
    targets: [
        .executableTarget(
            name: "lb3",
            path: "Sources/lb3"
        ),
        .testTarget(
            name: "lb3Tests",
            dependencies: ["lb3"],
            path: "Tests/lb3Tests"
        )
    ]
)
