
using Test
include(joinpath(@__DIR__, "..", "src", "Lab01.jl"))
using .Lab01

@testset "lab01" begin
    t, u = exponential_growth(0.3, 2.0; dt = 0.5)
    @test length(t) == 5
    @test u[end] > u[1]
end
