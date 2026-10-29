// swift-tools-version: 6.0
import PackageDescription

let package = Package(
    name: "lb1",
    platforms: [.macOS(.v13)],
    products: [
        .executable(name: "lb1", targets: ["lb1"])
    ],
    targets: [
        .executableTarget(
            name: "lb1",
            path: "Sources/lb1"
        ),
        .testTarget(
            name: "lb1Tests",
            dependencies: ["lb1"],  
            path: "Tests/lb1Tests"
        )
    ]
)
