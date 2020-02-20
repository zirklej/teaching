# -*- coding: utf-8 -*-
"""
Spyder Editor
"""

from matplotlib import pyplot as plt
import numpy as np

x=np.arange(-8,8,0.1)
y=np.arange(-8,8,0.1)
xx,yy=np.meshgrid(x,y)


# elliptic paraboloid
def ell_par():
    z1=(xx**2)+(yy**2)

    fig1=plt.figure(figsize=(12,6))
    ax1=fig1.add_subplot(1,1,1,projection='3d')
    ax1.plot_surface(xx,yy,z1)
    ax1.set_title("elliptic paraboloid")
    return

# hyperbolic paraboloid
def hyp_par():
    z2=(xx**2)-(yy**2)

    fig2=plt.figure(figsize=(12,6))
    ax2=fig2.add_subplot(1,1,1,projection='3d')
    ax2.plot_surface(xx,yy,z2)
    ax2.set_title("hyperbolic paraboloid, aka saddle")
    return

# ellipsoid
def ellip():
    coefs=(1,6,3)
    rx,ry,rz=1/np.sqrt(coefs)

    phi=np.linspace(0.,np.pi,100,endpoint=True)
    theta=np.linspace(0.,2*np.pi,100,endpoint=True)

    xx3=rx*np.outer(np.sin(phi),np.cos(theta))
    yy3=ry*np.outer(np.sin(phi),np.sin(theta))
    z3=rz*np.outer(np.cos(phi),np.ones_like(theta))

    fig3=plt.figure(figsize=(12,6))
    ax3=fig3.add_subplot(1,1,1,projection='3d')
    ax3.plot_surface(xx3,yy3,z3,cmap='viridis')
    ax3.set_title("ellipsoid")
    return

# hyperboloid of one sheet
def hyp_sht():
    coefs=(1,3,5)
    rx,ry,rz=1/np.sqrt(coefs)

    u=np.linspace(-5,5,100,endpoint=True)
    theta=np.linspace(0.,2*np.pi,100,endpoint=True)
    xx4=rx*np.outer(np.sqrt(1+u**2),np.cos(theta))
    yy4=ry*np.outer(np.sqrt(1+u**2),np.sin(theta))
    z4=rz*np.outer(u,np.ones_like(u))

    fig4=plt.figure(figsize=(12,6))
    ax4=fig4.add_subplot(1,1,1,projection='3d')
    ax4.plot_surface(xx4,yy4,z4)
    ax4.set_title("hyperboloid of one sheet")
    return

# cone
def cone():
    u=np.linspace(-5,5,100,endpoint=True)
    v=np.linspace(0,2*np.pi,100,endpoint=True)
    
    x=np.outer(u,np.cos(v))
    y=np.outer(u,np.sin(v))
    z=np.outer(u,np.ones_like(u))
    
    fig=plt.figure(figsize=(12,6))
    ax=fig.add_subplot(1,1,1,projection='3d')
    ax.plot_surface(x,y,z)
    ax.set_title("cone")
    return

# hyperboloid of two sheets
def hyp_2sht():
    coefs=(1,0.5,2)
    rx,ry,rz=1/np.sqrt(coefs)
        
    u=np.linspace(-2.5,2.5,101)
    v=np.linspace(0,np.pi,101)
    x=rx*np.outer(np.sinh(u),np.cos(v))
    y=ry*np.outer(np.sinh(u),np.sin(v))
    z=rz*np.outer(np.cosh(u),np.ones_like(u))
        
    fig=plt.figure(figsize=(12,6))
    ax=fig.add_subplot(1,1,1,projection='3d')
    ax.plot_surface(x,y,z)        
    ax.plot_surface(x,y,-z)
    ax.set_title("hyperboloid of two sheets")
    return
    
# no.51:  z=xy^2 at (2,3)
def fifty_one():
    x5=np.arange(0,5,0.01)
    y5=np.arange(0,5,0.01)
    xx5,yy5=np.meshgrid(x5,y5)
    z5=xx5*yy5**2
    z5_plane=18+9*(xx5-2)+12*(yy5-3)

    fig5=plt.figure(figsize=(12,6))
    ax5=fig5.add_subplot(1,1,1,projection='3d')
    ax5.plot_surface(xx5,yy5,z5,alpha=0.5)
    ax5.plot_surface(xx5,yy5,z5_plane,color='y',alpha=0.8)
    ax5.scatter(2,3,18,marker="o",s=30,color="r")
    ax5.set_title("# 51")
    return

# monkey saddle
def monkey():
    u=np.arange(-3,3,0.01)
    v=np.arange(-3,3,0.01)
    uu,vv=np.meshgrid(u,v)
    
    x=uu
    y=vv
    z=uu**3-3*uu*vv**2
    
    fig=plt.figure(figsize=(12,6))
    ax=fig.add_subplot(1,1,1,projection='3d')
    ax.plot_surface(x,y,z)
    ax.set_title("monkey saddle")
    return

# no.52:  z=x^2/y at (4,2)
def fifty_two():
    x6=np.arange(-5,5,0.03)
    y6=np.arange(-5,5,0.03)
    xx6,yy6=np.meshgrid(x6,y6)
    z6=(xx6**2)/yy6
    z6_plane=8+4*(xx6-4)-4*(yy6-2)

    fig6=plt.figure(figsize=(12,6))
    ax6=fig6.add_subplot(1,1,1,projection='3d')
    ax6.plot_surface(xx6,yy6,z6,alpha=0.5)
    ax6.plot_surface(xx6,yy6,z6_plane,color='y',alpha=0.5)
    ax6.scatter(4,2,8,marker="o",s=40,color='r')
    ax6.set_title("# 52")
    return

# unit sphere at origin with plane(s)
def sph():
    rho=3
    phi=np.linspace(0.,np.pi,100,endpoint=True)
    theta=np.linspace(0.,2*np.pi,100,endpoint=True)

    x=rho*np.outer(np.sin(phi),np.cos(theta))
    y=rho*np.outer(np.sin(phi),np.sin(theta))
    z=rho*np.outer(np.cos(phi),np.ones_like(theta))
    x_plane=np.arange(-3,3,0.1)
    y_plane=np.arange(-3,3,0.1)
    xx_plane,yy_plane=np.meshgrid(x_plane,y_plane)
    z_plane=9-2*xx_plane-2*yy_plane  # at point (2,2,1)
    
    fig=plt.figure(figsize=(12,6))
    ax=fig.add_subplot(1,1,1,projection='3d')
    ax.plot_surface(x,y,z,alpha=0.75)
    ax.plot_surface(x_plane,y_plane,z_plane,color='y',alpha=0.5)
    ax.scatter(2,2,1,s=40,marker='o',color='r')
    #ax.set_xlim(0,3)
    #ax.set_ylim(0,3)
    #ax.set_zlim(0,1.1)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    ax.set_title("sphere with tangent plane")
    return

def curv_int():
    phi=np.linspace(0.,np.pi/2,100,endpoint=True)
    theta=np.linspace(0.,np.pi/2,100,endpoint=True)
    
    x=np.outer(np.sin(phi),np.cos(theta))
    y=np.outer(np.sin(phi),np.sin(theta))
    z=np.outer(np.cos(phi),np.ones_like(theta))
    
    # curve of intersection with y=1/sqrt(2)
    x_curve=(1/np.sqrt(2))*np.cos(theta)
    y_curve=np.ones_like(phi)*1/np.sqrt(2)
    z_curve=(1/np.sqrt(2))*np.sin(theta)
    
    # tangent line at (0.5,1/sqrt(2),0.5)
    t=np.arange(-0.5,0.5,0.1)
    x_tangent=0.5+t*1
    y_tangent=1/np.sqrt(2)*np.ones_like(t)
    z_tangent=0.5-t
    
    # y=1/sqrt(2) plane
    x_plane=np.linspace(0,1,100,endpoint=True)
    z_plane=np.linspace(0,1,100,endpoint=True)
    xx_plane,zz_plane=np.meshgrid(x_plane,z_plane)
    y_plane=np.outer(1/np.sqrt(2),np.ones_like(x_plane))
    
    fig=plt.figure(figsize=(12,6))
    ax=fig.add_subplot(1,1,1,projection='3d')
    ax.plot_surface(x,y,z,alpha=0.5)    # surface
    ax.plot(x_curve,y_curve,z_curve,color='r',linewidth=2,) # curve of intersection
    ax.plot(x_tangent,y_tangent,z_tangent,color='g',linewidth=2,)   # tangent line
    ax.scatter(0.5,1/np.sqrt(2),0.5,marker='o',s=25,color='k')  # tangent point
    ax.plot_surface(xx_plane,y_plane,zz_plane,alpha=0.5)  # plane
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    ax.set_title('dz/dx at (0.5,1/sqrt(2),0.5)')
    return

#ell_par()
#hyp_par()
#ellip()
#hyp_sht()
#hyp_2sht()
#cone()

#monkey()
#curv_int()

#fifty_one()
#fifty_two()

sph()





















