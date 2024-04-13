#include <windows.h>
#include <GL/glut.h>
#include <stdlib.h>
#include <iostream>
using namespace std;
GLfloat ex = 0.0, ey = 0.0, ez = -3.0;
void init()
{
        glEnable(GL_DEPTH_TEST);
        glMatrixMode(GL_PROJECTION);
        glLoadIdentity();

        glFrustum(-4.0, 4.0, -4.0, 4.0, 1.0, 10.0);
        glOrtho(-4.0, 4.0, -4.0,  4.0, 1.0, 10.0);
        glMatrixMode(GL_MODELVIEW);
        glLoadIdentity();

        gluLookAt(ex, ey, ez,  0.0, 0.0, 0.0, 0.0, 1.0, 0.0);
}
/*
GLfloat vertices[8][3]={
    {-1.0, -1.0, 1.0},     {-1.0, 1.0, 1.0},    {1.0, 1.0, 1.0},
    {1.0, -1.0, 1.0},    {-1.0, -1.0, -1.0},     {-1.0, 1.0, -1.0},
    {1.0, 1.0, -1.0},    {1.0, -1.0, -1.0}
};

GLfloat colors[8][3]={
    {0.0, 0.0, 0.0},{1.0, 0.0, 0.0},
    {1.0, 1.0, 0.0},{0.0, 1.0, 0.0},
    {0.0, 0.0, 1.0},{1.0, 0.0, 1.0},
    {1.0, 1.0, 1.0},{0.0, 1.0, 1.0}
};

void quad(int a, int b, int c, int d)
{
    glBegin(GL_QUADS);
        glVertex3fv(vertices[a]);
        glVertex3fv(vertices[b]);
        glVertex3fv(vertices[c]);
        glVertex3fv(vertices[d]);
    glEnd();
}
void mydraw()
{
    glColor3f(1.0, 0.0, 0.0);
    glColor3fv(colors[6]);     quad(0, 3, 2, 1);
    glColor3fv(colors[1]);     quad(2, 3, 7, 6);
    glColor3fv(colors[2]);     quad(0, 4, 7, 3);
    glColor3fv(colors[3]);     quad(1, 2, 6, 5);
    glColor3fv(colors[4]);     quad(4, 5, 6, 7);
    glColor3fv(colors[5]);     quad(0, 1, 5, 4);
}
void drawObject()
{
    glColor3f(0.7, 0.0, 0.50);
    glutWireDodecahedron();
    glTranslated(2, 2,0);
    //glutSolidTorus(0.5, 1, 4, 20);
    //glutWireTorus(3, 5, 25, 25);
    //glColor3f(0.7, 0.7, 0);
    glutWireSphere(2,1,1);
    //glColor3f(0.0, 1.0, 1.0);
    //glTranslatef(-2.0, 1.0, 0);
    //glutWireTorus(0.5, 1, 30, 30);
    //glutWireTeapot(2.0);
    //glScalef(3.5, 3.5, 3.50);
    //glutWireCube(2.0);
    //glutWireTetrahedron();

    //glutWireOctahedron();
    //glBegin();
    //glEnd();

}*/
void resize(int width, int height)
{
    double aspect;
    glViewport(0, 0, width, height);
    aspect = (double) width / (double) height;
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    cout << "aspect ratio" << aspect;
    if (aspect < 1.0)
    {
        glOrtho(-4., 4., -4./aspect, 4./aspect, 1., 100.);
    }
    else
    {
        glOrtho(-4.*aspect, 4.*aspect, -4., 4., 1., 100.);
    }
    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();
    gluLookAt(0., 0., 5., 0., 0., 0., 0., 1., 0.);

}
void drawCar()
{

    // Draw Cuboid
    glColor3f(0.7, 0.0, 0.50);
    GLfloat width = 2.0;   // width of the cuboid
    GLfloat height = 1.0;  // height of the cuboid
    GLfloat depth = 1.5;   // depth of the cuboid

    // Draw the cuboid
    glPushMatrix();
    glScalef(width, height, depth);
    glutSolidCube(1.0); // Use glutWireCube for drawing the cuboid
    glPopMatrix();
    // Draw Spheres at each corner of the base
    glColor3f(0.0, 1.0, 1.0); // Set color for spheres

    // Adjustments for spheres at corners
    GLfloat sphere_radius = 0.8; // Radius of spheres


    glPushMatrix();
    glTranslatef(-1.0, -1.0, -1.0); // Bottom-left-front corner
    //glutWireTorus(sphere_radius-0.6, sphere_radius, 20, 15);
    glutWireSphere(sphere_radius, 10, 10);
    glPopMatrix();

    glPushMatrix();
    glTranslatef(-1.0, -1.0, 1.0); // Bottom-left-back corner
    glutWireSphere(sphere_radius, 10, 10);
    glPopMatrix();

    glPushMatrix();
    glTranslatef(1.0, -1.0, -1.0); // Bottom-right-front corner
    glutWireSphere(sphere_radius, 10, 10);
    glPopMatrix();

    glPushMatrix();
    glTranslatef(1.0, -1.0, 1.0); // Bottom-right-back corner
    glutWireSphere(sphere_radius, 10, 10);
    glPopMatrix();

    // Draw the second cuboid (top one)
    glColor3f(0.7, 0.0, 0.50);

    // Translation for the second cuboid
    GLfloat second_cuboid_height = 0.5; // height of the second cuboid
    GLfloat vertical_offset = height + second_cuboid_height / 2.0; // Offset to position the second cuboid above the first one

    glPushMatrix();
    glTranslatef(0.0, vertical_offset, 0.0); // Position the second cuboid above the first one
    glScalef(width, second_cuboid_height, depth); // Scale the second cuboid
    glutWireCube(1.0); // Use glutWireCube for drawing the second cuboid
    glPopMatrix();
}
void display(void)
{
    glClearColor(0.0f, 0.0f, 0.0, 0.0f);
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
    //drawObject();
    drawCar();
    glutSwapBuffers();
}


static void key(unsigned char key, int x, int y)
{
    switch (key)
    {
        case 27 :
        case 'q':
            exit(0);
            break;

        case '+':
            cout << "+" << "Pressed ";
            ez += 1.0;
            break;

        case '-':
            cout << "+" << "Pressed ";
            ez -= 1.0;
            break;
    }
    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();
    gluLookAt(ex, ey, ez,  0.0, 0.0, 0.0, 0.0, 1.0, 0.0);
    glutPostRedisplay();

}


static void arrowKey(int key, int x, int y)
{
    cout << key << "pressed\n";
    switch(key)
    {
        case GLUT_KEY_LEFT:
            cout << "GLUT_KEY_LEFT" << "Pressed ";
            ex -= 1.0;
            break;

        case GLUT_KEY_RIGHT:
            cout << "GLUT_KEY_RIGHT" << "Pressed ";
            ex += 1.0;
            break;

        case GLUT_KEY_UP:
            cout << "GLUT_KEY_UP" << "Pressed ";
            ey -= 1.0;
            break;

       case GLUT_KEY_DOWN:
            cout << "GLUT_KEY_DOWN" << "Pressed ";
            ey += 1.0;
            break;

    }
    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();
    gluLookAt(ex, ey, ez,  0.0, 0.0, 0.0, 0.0, 1.0, 0.0);
    glutPostRedisplay();
}

static void idle(void)
{
    glutPostRedisplay();
}


int main(int argc, char *argv[])
{
    glutInit(&argc, argv);
    glutInitWindowSize(640,480);
    glutInitWindowPosition(10,10);
    glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE | GLUT_DEPTH);

    glutCreateWindow("3D Projection");

    glutReshapeFunc(resize);
    glutDisplayFunc(display);
    glutKeyboardFunc(key);
    glutSpecialFunc(arrowKey);
    //glutIdleFunc(idle);

    init();

    glutMainLoop();

    return EXIT_SUCCESS;
}
