import React from "react";
import { List, message } from "antd";
import CardItems from "./components/Card";
import axios from "axios";
import OrderCards from "./components/OrderCards";
const data = [
	"Racing car sprays burning fuel into crowd.",
	"Japanese princess to wed commoner.",
	"Australian walks 100km after outback crash.",
	"Man charged over missing wedding girl.",
	"Los Angeles battles huge wildfires.",
];
const App = () => {
	const [state, setstate] = React.useState([]);
	const [orders, setOrders] = React.useState([]);
	const [loading, setloading] = React.useState(false);
	const BASE_URL = axios.create({
		baseURL: "http://127.0.0.1:8000",
		withCredentials: true,
	});
	const getMenuItems = async () => {
		setloading(true);
		try {
			let res = await BASE_URL.get("/api/menu/");
			// console.log("Response:", res.data);
			setstate(res.data.menu_items);
			setloading(false);
		} catch (error) {
			// console.log("Error:", error);
		}
	};

	const getOrdersItems = async () => {
		setloading(true);
		try {
			let res = await BASE_URL.get("/api/orders/");
			// console.log("Response:", res.data);
			if (res.data) {
				let orderMappingFromDishesIds = res.data.orders_items.map(
					(item) => {
						let dishes= item.dishes_ids.map((dishId) => {
              let dishItems = state.filter((item) => item.id === dishId);
              return dishItems[0];
						});
            // console.log("dishes:", dishes)
						return {
							...item,
							dishes,
						};
					}
				);
				// console.log(
				// 	"orderMappingFromDishesIds:",
				// 	orderMappingFromDishesIds
				// );
				setOrders(orderMappingFromDishesIds);
			}
			setloading(false);
		} catch (error) {
			console.log("Error:", error);
		}
	};
	React.useEffect(() => {
		getMenuItems();
	}, []);

  React.useEffect(() => {
    getOrdersItems();
  }, [state]);

	const handleEditAvailability = (id) => {
		console.log(id);
		message.success("Item is edited");
	};
	const handleDeleteItem = (id) => {
		console.log(id);
		message.success("Item is deleted");
	};
	return (
		<div style={{ display: "flex", width: "100%" }}>
			<List
				style={{
					width: 300,
					maxHeight: "100vh",
					minHeight: "100vh",
					overflow: "auto",
          marginRight: "10px"
				}}
				header={<div>Menu List</div>}
				// footer={<div>Footer</div>}
				bordered
				dataSource={state}
				renderItem={(item) => (
					<List.Item>
						<CardItems
							{...item}
							loading={loading}
							handleEditAvailability={handleEditAvailability}
							handleDeleteItem={handleDeleteItem}
						/>
					</List.Item>
				)}
			/>
			<List
				style={{
					width: 500,
					maxHeight: "100vh",
					minHeight: "100vh",
					overflow: "auto",
				}}
				header={<div>Orders List</div>}
				// footer={<div>Footer</div>}
				bordered
				dataSource={orders}
				renderItem={(item) => (
					<List.Item>
						<OrderCards
              key={item?._id}
							{...item}
							loading={loading}
							handleEditAvailability={handleEditAvailability}
							handleDeleteItem={handleDeleteItem}
						/>
					</List.Item>
				)}
			/>
		</div>
	);
};
export default App;
