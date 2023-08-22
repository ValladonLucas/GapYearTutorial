"""
Author : Lucas Valladon
Aim : Coding challenge 1
"""

######################## Importing libraries ########################
import argparse # To parse arguments
import itk # ITK library
import vtk # VTK library

######################## Parsing arguments ########################

parser = argparse.ArgumentParser()
parser.add_argument("input", type=str,
                    help="input image") # input image
parser.add_argument("output",  type=str,
                    help="output image") # output image
parser.add_argument("-f", "--filter", type=str, choices=["median", "threshold"], 
                    help="apply a filter to the image") # filter to apply
args = parser.parse_args()

######################## Reading input image ########################

input_filename = args.input

######################## Reading input image with ITK and converting it to a VTK image ########################

image = itk.imread(input_filename, itk.US) # itk.US: unsigned short, pixel type modification to fit with filter from ITK

######################## Applying a filter to the image ########################

if args.filter == "median":
    median = itk.median_image_filter(image, radius=2) # radius: size of the median filter
    itk.imwrite(median, args.output, compression=True) # Save image
elif args.filter == "threshold":
    threshold = itk.threshold_image_filter(image, lower=100, upper=200, outside_value=0)
    itk.imwrite(threshold, args.output, compression=True)


####################### Displaying the image with VTK renderer #######################

renderer = vtk.vtkRenderer() # Create a renderer

render_window = vtk.vtkRenderWindow() # Create a render window
render_window.AddRenderer(renderer) # Add the renderer to the render window

image_reader_input = vtk.vtkPNGReader() # Create a PNG reader
image_reader_input.SetFileName(args.input) # Set the input image
image_reader_input.Update() # Update the reader

image_reader_output = vtk.vtkPNGReader()
image_reader_output.SetFileName(args.output) # Set the output image
image_reader_output.Update()

image_actor_input = vtk.vtkImageActor() # Create an image actor
image_actor_input.SetInputData(image_reader_input.GetOutput()) # Set the input image

image_actor_output = vtk.vtkImageActor()
image_actor_output.SetInputData(image_reader_output.GetOutput())

transform_input = vtk.vtkTransform() # Create a transform
transform_output = vtk.vtkTransform()

transform_input.Translate(0, 0, 0) # Translate the input image
transform_output.Translate(image_reader_output.GetOutput().GetDimensions()[0], 0, 0)

image_actor_input.SetUserTransform(transform_input) # Set the transform to the input image
image_actor_output.SetUserTransform(transform_output)

renderer.AddActor(image_actor_input) # Add the image actor to the renderer
renderer.AddActor(image_actor_output)


######################## Add titles to the images ########################
# Add titles to the images
title1 = vtk.vtkTextActor()
title1.SetTextScaleModeToNone()
title1.SetPosition(20, 20)
title1.GetTextProperty().SetColor(1.0, 1.0, 1.0)  # Set text color to white
title1.GetTextProperty().SetFontSize(24)  # Set font size
title1.GetTextProperty().SetFontFamilyToArial()
title1.SetInput("Original image")

title2 = vtk.vtkTextActor()
title2.SetTextScaleModeToNone()
title2.SetPosition(image_reader_output.GetOutput().GetDimensions()[0] + 20, 20)
title2.GetTextProperty().SetColor(1.0, 1.0, 1.0)
title2.GetTextProperty().SetFontSize(24)
title2.GetTextProperty().SetFontFamilyToArial()
title2.SetInput("Filtered image")

renderer.AddActor2D(title1) # Add titles to the renderer
renderer.AddActor2D(title2)
###########################################################################


render_window_interactor = vtk.vtkRenderWindowInteractor() # Create a render window interactor
render_window_interactor.SetRenderWindow(render_window) # Set the render window to the render window interactor

render_window.Render() # Render the image
render_window_interactor.Start() # Start the render window interactor

