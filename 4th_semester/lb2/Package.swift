// swift-tools-version: 6.0
import PackageDescription

let package = Package(
    name: "lb2",
    platforms: [.macOS(.v13)],
    products: [
        .executable(name: "lb2", targets: ["lb2"])
    ],
    targets: [
        .executableTarget(
            name: "lb2",
            path: "Sources/lb2"
        ),
        .testTarget(
            name: "lb2Tests",
            dependencies: ["lb2"],
            path: "Tests/lb2Tests"
        )
    ]
)
