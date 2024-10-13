# layout-merchant
A repository of many Formula Student Driverless style layouts that can be used for benchmarking, testing, training etc. The layouts follow the style of tracks used in the Formula Student Driverless competition, but are not guaranteed to be rules compliant. For example, some tracks are longer than what the rules allow. They are useful for testing many scenarios in one layout and to check the limits of the speed of your algorithms for tracks that are longer than the competition tracks.

The reason for creating this repository is that for my master thesis I would have liked to have a standardized set of layouts to have as a benchmark for my algorithms. In the end I had to make my own layouts, trying to mimic the style of the Formula Student Driverless competition. I thought that it would be a good idea to share these layouts, so that others can use them for their own projects.

### File structure

The layouts are stored as `json` files with the following keys:
- `x`: The x-coordinate of the cones (center of the cone) (array of floats)
- `y`: The y-coordinate of the cones (center of the cone) (array of floats)
- `color`: The color of the cones as an int (array of ints) (0: unknown, 1: yellow, 2: blue, 3: orange_small, 4: orange_big)
- `start_position`: The starting position of the car (array of 2 floats)
- `start_orientation`: The starting orientation of the car in degrees (float)
- `timing_line_position`: The position of the timing line (array of 2 floats) 
- `timing_line_orientation`: The orientation of the timing line in degrees.  (float)
- `timing_line_width`: The width of the timing line (float)


### Track types

#### Automatically created tracks

Most of the layouts were created using my drawing tool [drawing-to-fsd-layout](https://drawing-to-fsd-layout.streamlit.app/). The tool is available as a web application and can be used to create your own layouts. The tool is also available as a Python package, so that you can create layouts programmatically.

#### Approximations of real tracks

There are four approximations of real competition tracks in the repository:
- `FSG19`: Made from [this video](https://www.youtube.com/watch?v=h22J8YzNdjo). Note that the outside cones of the last turn are not visible in the video, so they are placed manually.
- `FSS19`: Made from [this video](https://www.youtube.com/watch?v=9_wI5vHNGTA)
- `FSE22`: Made from [this video](https://youtu.be/Tj-euskTGgM?feature=shared&t=434)
- `FSG23`: Made from [this video](https://www.youtube.com/watch?v=9MWKDJeAEDU)

There are also two tracks presented by Ecurie Aix in their ARWo presentation which I have also converted:
- `ecurie_track_1`: Made from [this video](https://youtu.be/gzWSZGqz-Wo?feature=shared&t=267)
- `ecurie_track_2`: Made from [this video](https://youtu.be/gzWSZGqz-Wo?feature=shared&t=602)

A caveat for these layouts is that while the position of the cones relative to each other is correct, the scale of the track was guesstimated.

#### Skidpad and Acceleration

There are also layouts for the skidpad and acceleration events. These two tracks were created programmatically and should comply with the rules of the Formula Student Driverless competition.

