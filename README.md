# Water Bodies Extraction using Python & GeoPandas

This project demonstrates a complete workflow for detecting and extracting water bodies from satellite imagery using open‑source geospatial tools.  
It is designed as a portfolio example for GIS / Remote Sensing / Python positions and shows practical skills in raster processing, spectral analysis, and vectorization.

---

## 🚀 Project Overview

The goal of this project is to automatically identify water bodies from satellite data using Python.  
The workflow includes:

- Loading raster data (e.g., Sentinel‑2 bands)
- Computing a water index (NDWI)
- Thresholding and raster classification
- Converting raster water mask to vector polygons
- Cleaning and filtering results
- Exporting final GeoJSON/Shapefile layers

This pipeline can be adapted for environmental monitoring, hydrological studies, flood mapping, and land‑cover analysis.

---

## 🛰️ Data Sources

The project supports any multispectral imagery, including:

- **Sentinel‑2 L2A** (recommended)
- **Landsat 8/9**
- **Local GeoTIFF rasters**

Required bands for NDWI:

- **Green band** (e.g., B03 for Sentinel‑2)
- **NIR band** (e.g., B08 for Sentinel‑2)

---

## 🧰 Technologies & Libraries

This project uses the following Python stack:

- **geopandas**
- **rasterio**
- **numpy**
- **shapely**
- **matplotlib**
- **GDAL**
- **fiona**

---

## 📦 Project Structure

