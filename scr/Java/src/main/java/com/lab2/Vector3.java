package com.lab2;

public class Vector3 {
    float x;
    float y;
    float z;

    public Vector3(float x, float y, float z) {
        this.x = x;
        this.y = y;
        this.z = z;
    }

    public Vector3 sum(Vector3 v) {
        return new Vector3(this.x + v.x, this.y + v.y, this.z + v.z);
    }

    public Vector3 minus(Vector3 v) {
        return new Vector3(this.x - v.x, this.y - v.y, this.z - v.z);
    }

    public double abs() {
        return Math.sqrt(this.x * this.x + this.y * this.y + this.z * this.z);
    }

    public float scalar(Vector3 v) {
        return this.x * v.x + this.y * v.y + this.z * v.z;
    }

    public double angle(Vector3 v) {
        return Math.acos(this.scalar(v) / (this.abs() * v.abs()));
    }

    public Vector3 vector(Vector3 v) {
        return new Vector3(this.y * v.z - this.z * v.y, this.z * v.x - this.x * v.z, this.x * v.y - this.y * v.x);
    }

    public float getX() {
        return x;
    }

    public void setX(float x) {
        this.x = x;
    }

    public float getY() {
        return y;
    }

    public void setY(float y) {
        this.y = y;
    }

    public float getZ() {
        return z;
    }

    public void setZ(float z) {
        this.z = z;
    }
}
