
using Test
include(joinpath(@__DIR__, "..", "src", "Lab07.jl"))
using .Lab07

@testset "lab07" begin
    @test traffic_intensity(2.7, 1.0, 3) == 0.9
    @test traffic_intensity(1.8, 1.0, 2) < 1.0
end
