/* eslint-disable no-unused-vars */
import React from "react";
import { Button, message, Popconfirm } from "antd";
import { DeleteOutlined, EditOutlined } from "@ant-design/icons";
const confirm = (e) => {

};
const cancel = (e) => {
	// console.log(e);
	// message.error("Click on No");
};
const CustomeButton = ({ id, deleteButton, editButton, handleFunc }) => (
	<Popconfirm
		title={`Are you sure to ${deleteButton ? "delete" : "edit"} this task?`}
		description={deleteButton ? "This will delete the item" : "This will edit the item"}
		onConfirm={() => handleFunc(id)}
		onCancel={cancel}
		okText='Yes'
		// cancelText='No'
    >
		{deleteButton && <DeleteOutlined key='delete' />}
		{editButton && <EditOutlined key='edit' />}
	</Popconfirm>
);
export default CustomeButton;
