/* eslint-disable react/prop-types */
import React from "react";
import { Card, Skeleton } from "antd";
import { ShoppingCartOutlined } from "@ant-design/icons";
import CustomeButton from "./CustomeButton";
const { Meta } = Card;
const CardItems = ({
	loading,
	name,
	price,
	availability,
	id,
	handleEditAvailability,
	handleDeleteItem,

}) => {
	return (
		<Card
			style={{
				width: 300,
				marginTop: 16,
			}}
			actions={[
				<ShoppingCartOutlined key='shop' />,
				<CustomeButton
					key='edit'
					id={id}
					editButton
					handleFunc={handleEditAvailability}
				/>,
				<CustomeButton
					key='delete'
					id={id}
					deleteButton
					handleFunc={handleDeleteItem}
				/>,
			]}>
			<Skeleton loading={loading} avatar active>
				<Meta
					// avatar={
					// 	<Avatar src='https://xsgames.co/randomusers/avatar.php?g=pixel&key=2' />
					// }
					title={name}
					description={`$${price}`}
				/>
			</Skeleton>
		</Card>
	) 
};

export default CardItems;
