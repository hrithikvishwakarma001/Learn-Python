/* eslint-disable react/prop-types */
import React from 'react'
import { Card, Skeleton } from "antd";
import { ShoppingCartOutlined } from "@ant-design/icons";
import CustomeButton from "./CustomeButton";
import Meta from 'antd/es/card/Meta';
const OrderCards = ({
	customer_name,
	status,
	_id,
	dishes_ids,
	order_date,
	total_price,
	dishes,
  loading,
  handleEditAvailability,
  handleDeleteItem
}) => {
  // console.log("dishes:", dishes)
	return (
		<Card
			style={{
				width: 300,
				marginTop: 16,
				border: "1px solid #000",
			}}
			actions={[
				<ShoppingCartOutlined key='shop' />,
				<CustomeButton
					key='edit'
					id={_id}
					editButton
					handleFunc={handleEditAvailability}
				/>,
				<CustomeButton
					key='delete'
					id={_id}
					deleteButton
					handleFunc={handleDeleteItem}
				/>,
			]}>
			<Skeleton loading={loading} avatar active>
				<Meta
					// avatar={
					// 	<Avatar src='https://xsgames.co/randomusers/avatar.php?g=pixel&key=2' />
					// }
					title={customer_name}
					description={`$${total_price}`}
				/>
        <p style={{marginTop:"10px"}}>Dishes :</p>
				{dishes &&
					dishes.map((item) => (
						<Card
							key={item?.id}
							style={{
								width: 300,
								marginTop: 16,
								border: "1px solid #000",
							}}
							actions={[
								<ShoppingCartOutlined key='shop' />,
								<CustomeButton
									key='edit'
									id={item?.id}
									editButton
									handleFunc={handleEditAvailability}
								/>,
								<CustomeButton
									key='delete'
									id={item?.id}
									deleteButton
									handleFunc={handleDeleteItem}
								/>,
							]}>
							<Skeleton loading={loading} avatar active>
								<Meta
									// avatar={
									// 	<Avatar src='https://xsgames.co/randomusers/avatar.php?g=pixel&key=2' />
									// }
									title={item?.name}
									description={`$${item?.price}`}
								/>
							</Skeleton>
						</Card>
					))}
			</Skeleton>
		</Card>
	);
};

export default OrderCards
