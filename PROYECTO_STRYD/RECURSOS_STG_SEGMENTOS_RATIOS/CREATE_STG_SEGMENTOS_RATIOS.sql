
CREATE TABLE STG_SEGMENTOS_RATIOS(
FECHA				DATE			NULL,
CONTADOR			INT 			NULL,
SEGMENTO			INT 			NULL,
ID_TERRENO			INT				NULL,
ID_TIPOE			INT				NULL,
CP					INT 			NULL,
POTENCIA			INT 			NULL, 
POR_CP				DECIMAL(15,3)	NULL,
DISTANCIA			INT 			NULL,
DURACION			INT 			NULL,     
RITMO 				INT 			NULL,  
FREC_CARDIACA		INT 			NULL,   
CADENCIA 			INT 			NULL,
TSC  				INT 			NULL,  
FP 					INT 			NULL, 
LSS					DECIMAL(15,3) 	NULL, 
OSC_VERTICAL		DECIMAL(15,3) 	NULL,    
L_ZANCADA 			DECIMAL(15,3) 	NULL,
RFP					DECIMAL(15,3)	NULL,
RLSS				DECIMAL(15,3)	NULL,
ROV					DECIMAL(15,3)	NULL,
RE 					DECIMAL(15,3)	NULL,   
AIRE 				INT 			NULL,  
PENDIENTE			DECIMAL(15,3)	NULL,   
ALTITUD 			INT 			NULL, 
DESNIVEL			INT 			NULL, 
RSS					INT 			NULL,   
)
-- En esta tabla realizaremos el cálculo de alguno ratios que son necesarios e importantes como
-- métricas para el estudio de los enrenamientos y serán:
-- POR_CP: (POTENCIA/CP)*100
--          Ejemplo: (168/218) * 100 = 77,064.
-- RFP: (FP/POTENCIA) * 100
--          Ejemplo de aquí arriba, esto sería (71 FORM POWER/287 POWER) * 100 = 24,738.

--  				>25% está por debajo del promedio
-- 					23-25% está cerca del promedio
-- 					<23% es bueno
-- 					<20% es probablemente el reino de los corredores de élite de clase mundial

-- (LSS):Rigidez de resorte de la pierna 
-- 			RLSS: (LSS/PESO_STRYD) * 1000 = 154,878

-- 			La rigidez del resorte de la pierna es una medida de lo bien que un corredor recicla la energía aplicada al suelo. 
-- 			Se ha demostrado que el LSS está correlacionado con el rendimiento en la carrera. 
-- 			Piensa en tu pierna como un resorte sobre el cual tu cuerpo «rebota». 
-- 			Cuanto más rígido sea el resorte, menos energía deberá producir para impulsarse hacia adelante con cada paso. 
-- 			Esta métrica mide la rigidez de los músculos y tendones de la pierna. 
-- 			Los incrementos en el LSS pueden indicar una mejora en la economía con el tiempo. 
-- 			¿Cuál es un valor de LSS «bueno»? El LSS es individual y no puede ser comparado fácilmente entre diferentes corredores 
-- 			y debe ser estandarizado para el peso corporal en sus propias comparaciones a lo largo del tiempo. 
-- 			Por esta razón, las tendencias en LSS/kg para velocidades específicas deben ser el centro del análisis. 
-- 			Se ha demostrado que la movilidad dinámica y los ejercicios biomecánicos, junto con el entrenamiento de fuerza y los ejercicios 
-- 			de repetición en subida, mejoran la rigidez de las piernas y la economía de la carrera.
-- 			Dicho esto, el LSS para la mayoría de los atletas oscila entre 6 y 14 kN/M.

-- 					percentil 95								0.173
-- 					Por encima del promedio						0.158
-- 					Promedio									0.143
-- 					Por debajo del promedio						0.128
-- 					percentil 5									0.113

-- (OSC_VERTICAL):Oscilación vertical
--			ROV: (OSC_VERTICAL / L_ZANCADA)

--			La oscilación vertical mide la cantidad de «rebote», es decir, el movimiento vertical hacia arriba y hacia abajo, generado mientras corres. 
--			Similar al tiempo de contacto con el suelo, la aplicación de ejercicios, ejercicios pliométricos, fuerza y velocidad a su entrenamiento
--			y la monitorización de esta métrica a lo largo del tiempo puede ser el mejor enfoque para el análisis y seguimiento de las mejoras.
--			La magnitud de la oscilación vertical puede variar según la altura, la forma y la velocidad del corredor. 
--									Normalmente veo valores de 5 cm a 9 cm.
--			Sin embargo, como la mayoría de las métricas en ejecución, el contexto es importante. En el caso de la oscilación vertical, 
--			esto se hace mejor observando la oscilación vertical como una relación con la longitud de la zancada. Powercenter no proporciona 
--			la relación vertical (oscilación vertical en metros dividida por la longitud de la zancada en metros), pero es una buena manera de poner
--			la oscilación vertical en perspectiva. Una relación vertical del 5% de menos es bastante buena. 
--			Al igual que Form Power Ratio y Hortizontal Power Ratio, la relación vertical proporciona un vistazo de la vectorización 
--			del movimiento. Un valor más bajo para la relación vertical significa que se dirige más movimiento horizontalmente, 
--			en lugar de desperdiciarse verticalmente. Al igual que la relación de potencia de forma y su recíproca, 
--			la relación de potencia horizontal, la relación horizontal es la recíproca de la relación vertical. 
--			También como la relación de potencia horizontal, prefiero seguir la relación horizontal

-- (RE): Efectividad de Carrera Running Efectivesness
--			RE: (DISTANCIA / DURACION) / (POTENCIA/PESO_STRYD)
--					Ejemplo: (6000 m / 2833 s) / (185 w / 82 kg) = 0,938

--			RE es una métrica simple pero muy poderosa.  La ecuación es, simplemente:
--			RE = velocidad/potencia 
--			(donde la velocidad está en metros por segundo y la potencia en vatios por kilogramo)
--			Por tanto:   	RE = (m/s) / (W/kg)
-- 					RE = 0.99 a 1.01 está cerca del promedio
--					RE = <0.99 está por debajo del promedio
--					RE = >1.01 es bueno
--					RE => 1.05 es probablemente el reino de los corredores de élite de clase mundial



