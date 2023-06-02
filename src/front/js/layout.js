import React from "react";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import ScrollToTop from "./component/scrollToTop";

import { Home } from "./pages/home";
import { Demo } from "./pages/demo";
import { Single } from "./pages/single";
import injectContext from "./store/appContext";


import { Navbar } from "./component/navbar";
import { Footer } from "./component/footer";
//import  { Cards }  from "./component/cards.js";



// este componente Layout se encargará de enrutar las URL con todas las vistas de mi aplicación
const Layout = () => {
	//el nombre base(basename) se usa cuando su proyecto se publica en un subdirectorio y no en la raíz del dominio
	// puede establecer el nombre base en el archivo .env ubicado en la raíz de este proyecto, por ejemplo: BASENAME=/react-hello-webapp/
	const basename = process.env.BASENAME || "";

	return (
		<div>
			<BrowserRouter basename={basename}> 
			{/* todo lo que se coloque dentro de browserRouter,como por ejemplo Navbar, av a persistir en la vista de la interfaz independientemente de la ruta, se vera
			en todas las rutas */}
				<ScrollToTop>
					<Navbar/>
					
				{/* en routes se colocan todas las rutas que queremos envolcer (route), routes y route tenemos que importarlo al principio del documento */}
					<Routes> 
						{/* se coloca la ruta en path="/" en el cual cuando entremos en esa ruta especificamente nos lleva al componente que deseamos, nombrandolo en 
						( element={<Home /> podria ser cualquier otro componente}) Le dice a React que muestre la única <Route> que coincide con la URL mostrada. */}
						<Route path="/" element={<Home />} />  
						<Route path="/demo" element={<Demo />} />
						<Route path="/single/:theid" element={<Single />} />
						<Route path="/single/:type/:theid" element={<Single />} /> {/*es lo mismo que estamos colocando en card.js*/} 
						
						  {/* aqui iria la ruta dinamica ya que  tiene un añadido que dice: oye aunque las paginas sean iguales, en cada una quiero
																				 un tipo de datos diferentes. muy importante añadir los : para que react diga vale esto no es una palabra es una "caracteristica" */}
						<Route path="*" element={<h1>Not found!</h1>} /> 

					</Routes>
					<Footer />
				</ScrollToTop>
			</BrowserRouter>
		</div>
	);
};

export default injectContext(Layout);