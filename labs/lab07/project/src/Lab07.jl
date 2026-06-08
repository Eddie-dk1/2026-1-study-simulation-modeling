
module Lab07

export traffic_intensity

traffic_intensity(lambda::Float64, mu::Float64, c::Int) = lambda / (c * mu)

end
