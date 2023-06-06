const getState = ({ getStore, setStore }) => {
	return {
		store: {
			//aqui debo declarar un array de favoritos que se puedan agregar cuando el usuario lo desee,al igual que array de planets y character.

			characters: [],
			character:{},
			planets: [],
			planet:{},
			vehicles: [],
			vehicle:{},
			favorites: []
		},
		actions: {

			//personajes / characters
			fetchCharacters: () => {
				fetch("https://www.swapi.tech/api/people")
				
				.then(response => response.json()) // te trae un respuestas y la convierte en json
				.then(data => setStore({characters: data.results})) //la guaradara en u espacio de memoria llamado data. data.results en este caso es un array de elementos
																  //esos elementos son los que nos proporciona la url de swapi(result=[{"uid","name","url"}]    
				.catch(err => console.log()("request failed",err)); // si sale algo mal en alguno de los dos primeros pasos, aqui te mostraria el error.

			},
			//PERSONAJS DE MANERA INDIVIDUAL
			fetchCharacter: (id) => {
				fetch(`https://swapi.dev/api/people/${id}`)
				.then(response => response.json()) // te trae un respuestas y la convierte en json
				.then(data =>setStore({character: data})) //la guaradara en u espacio de memoria llamado data. data.results en este caso es un array de elementos
																  //esos elementos son los que nos proporciona la url de swapi(result=[{"uid","name","url"}]    
				.catch(err => console.log()("request failed",err)); // si sale algo mal en alguno de los dos primeros pasos, aqui te mostraria el error.

			},

			//PLANETAS
			 fetchPlanets: () => {
			 	fetch("https://www.swapi.tech/api/planets")
					.then(response => response.json()) // te trae un respuestas y la convierte en json
							 //setStore({propiedadDeStore:valor})
			 		.then(data => setStore({planets: data.results })) // esa respuesta la voy a guardar en un espacio de memoria que se llame "data" que a su vez se convertira en un objeto.
					.catch(err => console.log("request failed", err)); // si sale algo mal en alguno de los dos primeros pasos, aqui te mostraria el error.
			 },

			 fetchPlanet: (id) => {
				fetch(`https://swapi.dev/api/planets/${id}`)
				.then(response => response.json()) // te trae un respuestas y la convierte en json
				.then(data =>setStore({planet: data})) //la guaradara en u espacio de memoria llamado data. data.results en este caso es un array de elementos
																  //esos elementos son los que nos proporciona la url de swapi(result=[{"uid","name","url"}]    
				.catch(err => console.log()("request failed",err)); // si sale algo mal en alguno de los dos primeros pasos, aqui te mostraria el error.
			 },
          
			
			//VEHICULOS
			fetchVehicles:() => {
				fetch("https://www.swapi.tech/api/vehicles")
				.then(response => response.json())  // te trae un respuestas y la convierte en json
				.then(data => setStore({vehicles:data.results})) //la guaradara en u espacio de memoria llamado data. data.results en este caso es un array de elementos
																//esos elementos son los que nos proporciona la url de swapi(result=[{"uid","name","url"}] 
				.catch(err => console.log("request failed",err)); // si sale algo mal en alguno de los dos primeros pasos, aqui te mostraria el error.
			},
			//vehicles INDIVIDUAL
			fetchVehicle: (id) => {
  				fetch(`https://swapi.dev/api/vehicles/${id}`)
				.then(response => response.json())
				.then(data => setStore({ vehicle: data.result.properties }))
				.catch(err => console.log("Request failed", err));
},
			//AGREGAR A FAVORITOS
			 								
				addToFavorites:(name) =>{  //addToFavorites tomo un personaje como argumento(name) y su propiedad name
				const store=getStore()
				if (!store.favorites.includes(name)) {
					setStore({favorites:[...store.favorites,name]})
				} 
				else {
					let filtered = store.favorites.filter(favorite => favorite != name)
					setStore({favorites:filtered})
				}
				 //se obtiene el estado actual con store con los ateriores
				},
				
				//ELEMINAR DE FAVORITOS 
				deleteFavorite: (i) => {
					const store = getStore();
					const newList = store.favorites.filter((index) => index !== i);
					setStore({ favorites: newList });
				}
				
		}
	}
};


export default getState;