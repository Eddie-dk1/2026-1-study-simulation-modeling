
using Test
include(joinpath(@__DIR__, "..", "src", "Lab03.jl"))
using .Lab03

@testset "lab03" begin
    black, white, temp = daisyworld_point(1.0)
    @test black >= 0
    @test white >= 0
    @test temp > 0
end
