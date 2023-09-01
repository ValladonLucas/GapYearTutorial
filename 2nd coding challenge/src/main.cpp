#include <itkImage.h>
#include <itkImageFileReader.h>

#include <vtkImageActor.h>
#include <vtkImageReader2.h>
#include <vtkRenderer.h>
#include <vtkRenderWindow.h>
#include <vtkRenderWindowInteractor.h>
#include <vtkSmartPointer.h>



int main() {

    //////////////////// Image reading with ITK ////////////////////

    typedef itk::Image<unsigned char, 2> ImageType; // 2D image with unsigned char pixel type
    typedef itk::ImageFileReader<ImageType> ReaderType; // image reader type

    ReaderType::Pointer reader = ReaderType::New(); // create a reader
    reader->SetFileName("/home/lucas/Documents/Césure/GapYearTutorial/2nd coding challenge/src/hand.png"); // set the input file name

    try { // try to read the image
        reader->Update();
    } catch (itk::ExceptionObject &ex) {
        std::cerr << "Exception caught while reading the image:\n" << ex << std::endl;
        return EXIT_FAILURE;
    }

    ImageType::Pointer image = reader->GetOutput(); // get the output image
    std::cout << "Size: " << image->GetLargestPossibleRegion().GetSize() << std::endl; // print the size of the image

    //////////////////// Image displaying with VTK ////////////////////

    vtkSmartPointer<vtkImageReader2> readerVTK = vtkSmartPointer<vtkImageReader2>::New(); // create a reader
    readerVTK->SetFileName("/home/lucas/Documents/Césure/GapYearTutorial/2nd coding challenge/src/hand.png"); // set the input file name
    readerVTK->Update(); // read the image

    vtkSmartPointer<vtkImageActor> actor = vtkSmartPointer<vtkImageActor>::New(); // create an actor
    actor->SetInputData(readerVTK->GetOutput()); // set the input image

    vtkSmartPointer<vtkRenderer> renderer = vtkSmartPointer<vtkRenderer>::New(); // create a renderer
    renderer->AddActor(actor); // add the actor to the renderer

    vtkSmartPointer<vtkRenderWindow> renderWindow = vtkSmartPointer<vtkRenderWindow>::New(); // create a render window
    renderWindow->AddRenderer(renderer); // add the renderer to the render window

    vtkSmartPointer<vtkRenderWindowInteractor> renderWindowInteractor = vtkSmartPointer<vtkRenderWindowInteractor>::New(); // create a render window interactor
    renderWindowInteractor->SetRenderWindow(renderWindow); // set the render window to the render window interactor

    renderWindow->Render(); // render the image
    renderWindowInteractor->Start(); // start the window



    return 0;
}