import React, { useEffect, useState } from "react";
import { Container, DashboardContainer} from './styles';

import axios from 'axios';

const restaurantNames = ["Pampulha 1", "Pampulha 2", "Campus Saúde", "Campus Direito", "Campus ICA"];
const mealPeriod = "Almoco";  // ou "Jantar" conforme necessário

interface MenusType {
    [key: string]: string[];
  };

export function Dashboard() {
    
    const [menus, setMenus] = useState<MenusType>({})

    useEffect(() => {
        const fetchMenus = async () => {
            const fetchedMenus: MenusType = {};
            for (const restaurant of restaurantNames) {
                try {
                    const response = await axios.get('http://127.0.0.1:5000/menu', {
                        params: { restaurant_name: restaurant, meal_period: mealPeriod },
                    });
                    fetchedMenus[restaurant] = response.data.menu;
                } catch (error) {
                    console.error(`Erro ao buscar o menu para ${restaurant}:`, error);
                    fetchedMenus[restaurant] = ["Menu não disponível"];
                }
            }
            setMenus(fetchedMenus);
        }

        fetchMenus();
    }, [])

    return (
        <Container>
            <DashboardContainer>
            {/* Quatro cardápios (colunas) */}
                {restaurantNames.map((restaurant, index) => (
                    <div className="menu-card" key={index}>
                        <h2>{restaurant}</h2>
                        <ul>
                            {(menus[restaurant] || []).map((item: String, idx: number) => (
                            <li key={idx}>{item}</li>
                            ))}
                        </ul>
                    </div>
                ))}
            </DashboardContainer>
        </Container>
    );
}