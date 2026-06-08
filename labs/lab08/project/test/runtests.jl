
using Test
include(joinpath(@__DIR__, "..", "src", "Lab08.jl"))
using .Lab08

@testset "lab08" begin
    rate = total_rate(180, 6, 0.5, 0.18, 186)
    @test rate > 0
    @test total_rate(0, 0, 0.5, 0.18, 186) == 0
end
