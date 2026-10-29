// swift-tools-version: 6.0
import PackageDescription

let package = Package(
    name: "lb4",
    platforms: [.macOS(.v13)],
    products: [
        .executable(name: "lb4", targets: ["lb4"])
    ],
    targets: [
        .executableTarget(
            name: "lb4",
            path: "Sources/lb4"
        ),
        .testTarget(
            name: "lb4Tests",
            dependencies: ["lb4"],
            path: "Tests/lb4Tests"
        )
    ]
)
