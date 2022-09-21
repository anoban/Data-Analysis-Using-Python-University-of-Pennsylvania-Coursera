B
    �O_
  �               @   s   d dl Zd dlZdd� ZdS )�    Nc          	   C   sz  t �d�at�d�at�d�at�d�at jttdddd�at jttdd	dd�ad
d lm	a
 ttd dk atd d }t
j|td dddddd� ttd dk  atd d }t
j|td dddddd� t
�d� t
�d� t
jdd� d
d lm	a ttd dk attd dk atd }td }tj|dd d!d"� tj|dd#d$d"� t�d%� t�d&� tjdd� t�d'� d S )(Nz	imdb.xlsxZimdbZ	directorsZ	countries�innerZ
country_id�id)�left�rightZhowZleft_onZright_onZdirector_idr   Z
title_yeari�  Zgrossi@B Z
imdb_score�o�bgffffff�?�2   z
after 2000)Zmarker�color�alpha�s�label�rzbefore 2000zGross (Millions)ZRatingZbest)ZlocZcontent_rating�RzPG-13g      �?ZredzR-Rated Movies)r
   r	   r   ZbluezPG-13 Moviesz
IMDB ScoreZCountz,Score Distribution of R-Rated & PG-13 Movies)�pdZ	ExcelFileZxls�parseZdfZdf_directorsZdf_countries�mergeZmatplotlib.pyplotZpyplotZplt1Zdf_after_2000ZscatterZdf_before_2000ZxlabelZylabelZlegendZplt2Zdf_RZdf_PG13Zhist�title)�filepathZx1Zx2Zseries_RZseries_PG13� r   �./home/jovyan/work/source/Module 9/solutions.py�get_solutions   sB    









r   )Zpandasr   ZnumpyZnpr   r   r   r   r   �<module>   s   